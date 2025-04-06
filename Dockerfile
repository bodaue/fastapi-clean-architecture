FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi

COPY . .

CMD ["sh", "-c", "uvicorn app.main:app --host $SERVER_HOST --port $SERVER_PORT"]