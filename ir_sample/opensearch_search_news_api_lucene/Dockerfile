FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

RUN apt-get update && \
    apt-get install -y git sudo mecab libmecab-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY src /opt/app
WORKDIR /opt/app

ENTRYPOINT [ "bash", "api/docker-entrypoint.sh" ]
