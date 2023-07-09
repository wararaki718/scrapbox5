FROM amazonlinux:2

RUN yum update -y
RUN yum install yum-utils tar gzip wget make gcc openssl-devel bzip2-devel libffi-devel gcc-c++ -y

RUN yum -y install initscripts
RUN yum install systemd-sysv -y
RUN amazon-linux-extras install -y docker

# python
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz
RUN tar xzf Python-3.9.16.tgz

WORKDIR /opt/Python-3.9.16
RUN /opt/Python-3.9.16/configure --enable-optimizations
RUN make altinstall
RUN rm -f /opt/Python-3.9.16.tgz

# libraries
RUN pip3.9 install fastapi uvicorn docker-compose

COPY front /app
WORKDIR /app

RUN docker-compose build

EXPOSE 8080

ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]
