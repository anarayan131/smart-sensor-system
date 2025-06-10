FROM python:3.10-slim
WORKDIR /app
COPY sensor.py .
CMD ["python", "sensor.py"]