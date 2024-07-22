from os import environ
from typing import Final

# Initialize ONNX model
MODEL_PATH: Final[str] = environ.get(
    'ML_MODEL_PATH', default='./devops/ml_model_files/efficientnet-lite4-11.onnx',
)

LABELS_PATH: Final[str] = environ.get(
    'LABELS_PATH', default='./devops/ml_model_files/labels_map.txt',
)