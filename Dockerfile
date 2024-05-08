FROM python:3.12-alpine

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY test1.py /app

CMD ["python", "test1.py"]
