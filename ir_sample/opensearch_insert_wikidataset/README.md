# insert wikipedia dataset to opensearch

## setup

```shell
pip install opensearch-py tensorflow tensorflow-datasets transformers fugashi torch unidic-lite scikit-learn
```


## launch OpenSearch

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
