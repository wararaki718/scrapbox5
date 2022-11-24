# sagemaker training jobs

## setup

```shell
pip install sagemaker scikit-learn boto3
```

## prepare

generate data

```shell
python data.py
```

upload s3 bucket

```shell
aws s3 cp iris.csv ...
```

## run

open main.ipynb on your sagemaker notebook.
