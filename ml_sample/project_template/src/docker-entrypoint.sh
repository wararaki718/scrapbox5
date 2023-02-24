#!/bin/bash

if [ "$1" = "train" ]; then
    poetry run python batch/main.py
else
    poetry run uvicorn api.serve:app --host 0.0.0.0 --port 8080
fi
