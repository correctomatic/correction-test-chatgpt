FROM python:3.12-alpine

ARG LLM_PROVIDER=groq
ARG API_KEY
ARG MODEL

# Made available as environment variables in the container
# They can be overridden when running the container.
ENV LLM_PROVIDER=${LLM_PROVIDER}
ENV MODEL=${MODEL}
ENV API_KEY=${API_KEY}

WORKDIR /app

# Two different COPY commands are used to take advantage of
# Docker's caching mechanism. Requirements are less likely to
# change than the rest of the code, so they are copied first.
COPY ./app/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY ./exercise/prompt.txt /

CMD ["python", "correct_exercise.py"]
