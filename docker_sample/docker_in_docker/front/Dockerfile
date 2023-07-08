FROM python:3.10

RUN pip install fastapi uvicorn

COPY back /app
WORKDIR /app

EXPOSE 3000

ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
