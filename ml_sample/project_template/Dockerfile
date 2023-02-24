FROM python:3.8

RUN pip install poetry

COPY src /opt/ml/app
WORKDIR /opt/ml/app

RUN poetry install

ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
