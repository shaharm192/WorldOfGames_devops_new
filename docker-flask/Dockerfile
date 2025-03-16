FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
ENV FLASK_APP=docker_backend_testing.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python", "docker_backend_testing.py"]
