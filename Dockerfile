FROM python:3.10-slim
WORKDIR /app
COPY sensor.py .
CMD ["python3", "sensor.py"]