# grpc

## setup

```shell
pip install grpcio
```

## generate grcp code

```shell
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/helloworld.proto
```

## launch server

```shell
python server.py
```

## run client

```shell
python client.py
```
