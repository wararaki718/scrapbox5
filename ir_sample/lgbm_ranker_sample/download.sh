#!/bin/bash

## download data
wget -P data https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.train
wget -P data https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.train.query
wget -P data https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.test
wget -P data https://raw.githubusercontent.com/microsoft/LightGBM/master/examples/lambdarank/rank.test.query

echo "download complete"