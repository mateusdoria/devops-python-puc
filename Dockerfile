# Dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install boto3

CMD ["python", "main.py"]
