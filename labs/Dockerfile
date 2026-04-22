FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt
#Lưu hết vào container
COPY . .
#Báo cho Docker API này chạy cổng 8000
EXPOSE 8000
#Khởi động server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
