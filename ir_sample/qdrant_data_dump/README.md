# qdrant data dump

## setup

```shell
pip install qdrant-client numpy
```

## run

create a snapshot

```shell
docker-compose up
```

```shell
python main.py
```

after that, stop the docker container

```shell
docker-compose down
```

relaunch the container

```shell
docker-compose -f docker-compose.yml -f docker-compose.snapshot.yml up
```

```shell
python main.py
```
