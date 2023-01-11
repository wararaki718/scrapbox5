#!/bin/bash

mkdir -P dataset

wget -P ./dataset https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.test
wget -P ./dataset https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.train
wget -P ./dataset https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.test.query
wget -P ./dataset https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.train.query

echo "DONE"
