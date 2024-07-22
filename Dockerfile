FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*


# Copy the application files
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt