# keep alive

## setup

```shell
pip install httpx
```

## run

launch servers

```shell
docker-compose up
```

```shell
curl -I localhost:8000
```

```shell
python -m http.server 8080
```

```shell
curl -I localhost:8080 -H 'Connection:Keep-Alive'
```

```shell
```

```shell
python main.py
```
