FROM python:3.12

WORKDIR /app
COPY app/pyproject.toml app/poetry.lock* ./

RUN pip install -U pip
RUN pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi
COPY . .
ENTRYPOINT ["poetry", "run"]
CMD poetry run uvicorn main:app --host 0.0.0.0 --port ${HTTP_PORT} --reload