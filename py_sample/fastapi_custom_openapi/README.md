# use custom openapi

## setup

```shell
pip install fastapi uvicorn PyYAML
```

## run

generate openapi schema yaml

```shell
python main.py
```

launch api

```shell
uvicorn main:app
```

open http://localhost:8000/docs on your browser.
