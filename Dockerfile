FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*


# Copy the application files
COPY ./app /app/app
COPY ./efficientnet-lite4-11.onnx /app
COPY ./labels_map.txt /app
COPY ./requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt