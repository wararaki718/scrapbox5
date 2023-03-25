FROM qdrant/qdrant:v1.0.3

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install qdrant-client numpy

COPY . .

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
