FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn numpy pandas

CMD ["python", "main.py"]
