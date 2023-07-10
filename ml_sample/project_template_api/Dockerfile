FROM python:3.10

RUN pip install poetry

COPY src /opt/ml
WORKDIR /opt/ml

RUN poetry install

ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
