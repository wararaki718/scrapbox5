# news search with api

## setup environment

```shell
pip install opensearch-py transformers fugashi torch unidic-lite fastapi uvicorn
```

## download dataset

```shell
wget -P data https://raw.githubusercontent.com/tanreinama/Japanese-Fakenews-Dataset/master/fakenews.csv
```

## launch apps

launch opensearch and api

```shell
docker-compose up
```

check

```shell
curl -XGET --insecure -u 'admin:admin' 'https://localhost:9200'
```

## run

create an index and insert data

```shell
docker-compose -f docker-compose.batch.yml up
```

open http://localhost:8080/docs on your browser.
