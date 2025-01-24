FROM python:3.13 AS python-base

ARG HOST
ARG NUM_WORKERS

RUN mkdir ip_knowledge_base

WORKDIR /ip_knowledge_base

COPY /pyproject.toml /ip_knowledge_base

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY . .

CMD gunicorn -w ${NUM_WORKERS} -k uvicorn.workers.UvicornWorker app.main:app --bind ${HOST}:8000
