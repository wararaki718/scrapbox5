FROM python:3.5

RUN pip install nmslib==2.1.1

COPY src/batch /opt/app/batch
WORKDIR /opt/app

CMD ["python", "batch/main.py"]
