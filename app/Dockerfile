FROM python:3.12

WORKDIR /app
COPY app/pyproject.toml app/poetry.lock* ./

RUN pip install -U pip
RUN pip install poetry

RUN poetry install --no-root
COPY . .

CMD poetry run uvicorn main:app --host 0.0.0.0 --port ${HTTP_PORT} --reload