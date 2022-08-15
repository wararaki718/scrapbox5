# news search

## setup environment

```shell
pip install opensearch-py
```

## download dataset

```shell
wget -P data https://raw.githubusercontent.com/tanreinama/Japanese-Fakenews-Dataset/master/fakenews.csv
```

## build

```shell
docker-compose build
```

check plugins

```shell
curl -XGET --insecure -u 'admin:admin' 'https://localhost:9200/_cat/plugins?v'
```

## launch search engine

```shell
docker-compose up
```

check

```shell
curl -XGET --insecure -u 'admin:admin' 'https://localhost:9200'
```

## run

```shell
python main.py
```