# sharding

## setup

```shell
pip install transformers
```

## download

```shell
wget -P data https://jmcauley.ucsd.edu/data/amazon_v2/categoryFiles/Gift_Cards.json.gz --no-check-certificate
```

```shell
gzip -d data/Gift_Cards.json.gz
```

## run

```shell
docker-compose up
```

```shell
python main.py
```

check

```shell
python test.py
```
