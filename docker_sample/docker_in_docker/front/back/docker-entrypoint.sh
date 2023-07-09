#!/bin/bash

set -e

systemctl start docker
systemctl enable docker

uvicorn main:app --host 0.0.0.0 --port 3000
