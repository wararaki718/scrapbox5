# build multi-cluster

## run

```shell
docker-compose up
```

## check

```shell
curl http://localhost:6333/cluster | jq
```

memo

- raft で node cluster が１つ落とされる？？
