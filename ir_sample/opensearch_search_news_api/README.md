# news search with api

## setup environment

```shell
pip install opensearch-py transformers fugashi torch unidic-lite fastapi uvicorn
```

## download dataset

```shell
wget -P data https://raw.githubusercontent.com/tanreinama/Japanese-Fakenews-Dataset/master/fakenews.csv
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

create an index and insert data

```shell
bash batch-entrypoint.sh
```

api

```shell
bash api-entrypoint.sh
```

open http://localhost:8080/docs on your browser.
