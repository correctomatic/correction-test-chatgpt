FROM python:3.12-alpine

WORKDIR /app

COPY ./app /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./exercise/prompt.txt /app

CMD ["python", "correct_exercise.py"]
