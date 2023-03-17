# qdrant comment search

## setup

```shell
pip install qdrant-client numpy pandas transformers
```

## download

```shell
wget -P data https://raw.githubusercontent.com/amazon-science/amazon-multilingual-counterfactual-dataset/main/data/JP_train.tsv
```

## run

launch qdrant

```shell
docker-compose up
```

```shell
python main.py
```
