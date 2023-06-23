# gunicorn with fastapi

## setup

```shell
pip install gunicorn fastapi uvicorn[standard]
```

## run

```shell
gunicorn api.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```
