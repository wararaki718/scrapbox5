#!/bin/bash

set -e

docker-compose up -d

uvicorn main:app --host 0.0.0.0 --port 8080
