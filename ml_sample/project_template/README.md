# titanic classifier

## download

```shell
wget -P data https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
```

## build

```shell
docker-compose build
```

## run

batch

```shell
docker-compose -f docker-compose.yml -f docker-compose.batch.yml up
```

api

```shell
docker-compose -f docker-compose.yml -f docker-compose.api.yml up
```

## test

```shell
docker-compose -f docker-compose.yml -f docker-compose.test.yml up
```
