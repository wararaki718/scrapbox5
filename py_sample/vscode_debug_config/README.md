# debug settings

## use

copy launch.json to .vscode/launch.json

after that execute the code on your vscode

## setup

```shell
pip install uvicorn fastapi poetry
```

## run

app

```shell
python app/main.py
```

server

```shell
uvicorn server.main:app
```

poetry

```shell
poetry run python sample/main.py
```
