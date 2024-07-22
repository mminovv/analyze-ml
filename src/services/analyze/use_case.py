import json
import os
from uuid import UUID
import aiofiles

import cv2  # noqa
import ffmpeg  # noqa
import numpy as np
import onnxruntime as rt
from fastapi import UploadFile

from src.core.path import LABELS_PATH, MODEL_PATH
from src.infra.db.models.analyze import AnalyzeHistory
from src.interfaces.repositories.db.analyze_history import AnalyzeHistoryRepository


class AnalyzeService:
    def __init__(
        self,
        analyze_history_repo: AnalyzeHistoryRepository,
    ):
        self.analyze_history_repo = analyze_history_repo

    @staticmethod
    def _decode_video(video_path: str) -> list[np.ndarray]:
        """
        Decode a video file into a list of frames (numpy arrays) using ffmpeg.

        :param video_path:
        :return:
        """
        probe = ffmpeg.probe(video_path)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

        if video_stream is None:
            raise ValueError('No video stream found')

        width = int(video_stream['width'])
        height = int(video_stream['height'])

        process = (
            ffmpeg
            .input(video_path)
            .output('pipe:', format='rawvideo', pix_fmt='rgb24')
            .run_async(pipe_stdout=True)
        )
        frames = []
        while True:
            in_bytes = process.stdout.read(width * height * 3)
            if not in_bytes:
                break
            frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])
            frames.append(frame)
        return frames

    @staticmethod
    def _preprocess_image(image: np.ndarray) -> np.ndarray:
        """
        Preprocess an image for inference.

        :param image:
        :return:
        """
        image = cv2.resize(image, (224, 224))
        image = image.astype(np.float32)
        image = (image - 127.0) / 128.0

        return np.expand_dims(image, axis=0)

    def _analyze_frame(self, frame: np.ndarray) -> dict:
        """
        Analyze a single frame using the model.
        :param frame:
        :return:
        """
        model_session = rt.InferenceSession(MODEL_PATH)

        # Load labels
        with open(LABELS_PATH) as f:
            labels = json.load(f)

        input_image = self._preprocess_image(frame)
        results = model_session.run(["Softmax:0"], {"images:0": input_image})[0]

        top_results = np.argsort(results[0])[-5:][::-1]
        top_classes = [labels[str(idx)] for idx in top_results]
        top_probabilities = [float(results[0][idx]) for idx in top_results]  # Convert numpy.float32 to float

        return dict(classes=top_classes, probabilities=top_probabilities)

    async def __call__(self, *args, file: UploadFile, id: UUID, **kwargs):
        """
        Analyze a video file and save the results.
        :param args:
        :param file:
        :param request_id:
        :param kwargs:
        :return:
        """
        video_path = f"/tmp/{id}_{file.filename}"

        async with aiofiles.open(video_path, "wb") as f:
            await f.write(await file.read())

        frames = self._decode_video(video_path)
        results = [self._analyze_frame(frame) for frame in frames]

        analyze_history = AnalyzeHistory(
            id=id,
            result=json.dumps(results)
        )

        await self.analyze_history_repo.save(
            analyze_history
        )

        os.remove(video_path)


class GetAnalyzeByRequestIdService:

    def __init__(self, analyze_history_repo: AnalyzeHistoryRepository):
        self.analyze_history_repo = analyze_history_repo

    async def __call__(self, *args, request_id: UUID, **kwargs):
        analyze_history = await self.analyze_history_repo.get_analyze_by_id(request_id)

        if not analyze_history:
            return dict(detail="Result not found")

        return dict(result=json.loads(analyze_history.result))


class DeleteAnalyzeByRequestIdService:

    def __init__(self, analyze_history_repo: AnalyzeHistoryRepository):
        self.analyze_history_repo = analyze_history_repo

    async def __call__(self, *args, request_id: UUID, **kwargs):
        await self.analyze_history_repo.delete_analyze_history(request_id)
        return dict(detail="Result deleted")
