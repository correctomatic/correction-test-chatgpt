FROM python:3.12-alpine

WORKDIR /app

COPY ./app /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./exercise/prompt.txt /app

# Uncomment the line below to use the corresponding LLM provider
# by default. You can also set the LLM_PROVIDER environment
# when running the container to use a different provider.
ENV LLM_PROVIDER=g4f
# ENV LLM_PROVIDER=groq

CMD ["python", "correct_exercise.py"]
