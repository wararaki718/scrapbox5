# keep alive

## setup

```shell
pip install httpx
```

## run

launch servers

```shell
python -m http.server 8080
```

check connection

```shell
curl -v localhost:8080 localhost:8080 -H 'Connection:Keep-Alive'
```

run

```shell
python main.py
```
