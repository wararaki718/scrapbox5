FROM python:3.9

RUN pip install uvicorn==0.18.2 fastapi==0.79.0 PyYAML==5.3.1 --no-cache-dir
COPY src /opt/app

WORKDIR /opt/app
ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
