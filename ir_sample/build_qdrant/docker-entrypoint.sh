#!/bin/bash

./qdrant &

sleep 5

cd app

python3 main.py

echo "DONE"
