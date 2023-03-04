#!/bin/bash

if [ "$1" = "train" ]; then
    poetry run batch-runner
else
    poetry run api-runner
fi
