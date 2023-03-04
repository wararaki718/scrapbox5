#!/bin/bash

if [ "$1" = "train" ]; then
    poetry run python project_template/batch/main.py
else
    poetry run uvicorn project_template.api.serve:app --host 0.0.0.0 --port 8080
fi
