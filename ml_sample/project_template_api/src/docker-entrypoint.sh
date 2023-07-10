#!/bin/bash

poetry run uvicorn project_template.main:app --host 0.0.0.0 --port 8000
