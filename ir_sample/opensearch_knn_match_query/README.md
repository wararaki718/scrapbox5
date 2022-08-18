# news search by using knn & query

## setup environment

```shell
pip install opensearch-py transformers fugashi torch unidic-lite
```

## download dataset

```shell
wget -P batch/data https://raw.githubusercontent.com/tanreinama/Japanese-Fakenews-Dataset/master/fakenews.csv
```

## build custom opensearch

```shell
docker-compose build
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
cd batch
python main.py
```