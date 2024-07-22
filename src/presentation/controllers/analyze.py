from uuid import UUID, uuid4

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, UploadFile, File, BackgroundTasks

from src.services.analyze.dto.response import AnalyzeResponseModel, GetAnalyzeResponseModel
from src.services.analyze.use_case import AnalyzeService, GetAnalyzeByRequestIdService, DeleteAnalyzeByRequestIdService

analyze = APIRouter(prefix='/ext_gate', tags=['admin'], route_class=DishkaRoute)


@analyze.post("/analyze/{request_id}/", response_model=AnalyzeResponseModel)
async def analyze_image_or_video(
    service: FromDishka[AnalyzeService],
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks
):
    """
    Controller to analyze an image or video file and return the request_id
    I use background_tasks to run the service in the background for example.
    In production, it is necessary to run the service in the background to avoid blocking
    the main thread of the application. and you need to use a task queue like Celery or ARQ.
    I prefer to use ARQ because it is more modern and has better performance.

    :param service:
    :param file:
    :param background_tasks:
    :return:
    """
    request_id = uuid4()
    background_tasks.add_task(await service(file=file, id=request_id))
    return dict(request_id=request_id)


@analyze.get("/get_analysis/{request_id}/", response_model=GetAnalyzeResponseModel)
async def get_analysis(
    service: FromDishka[GetAnalyzeByRequestIdService],
    request_id: UUID,
):
    return await service(request_id=request_id)


@analyze.delete("/delete_analysis/{request_id}/")
async def delete_analysis(
    service: FromDishka[DeleteAnalyzeByRequestIdService],
    request_id: UUID,
):
    return await service(request_id=request_id)
