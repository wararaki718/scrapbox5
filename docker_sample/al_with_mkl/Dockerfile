FROM amazonlinux:2

RUN yum update -y
RUN yum install yum-utils tar gzip wget make gcc openssl-devel bzip2-devel libffi-devel gcc-c++ -y

# python
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz
RUN tar xzf Python-3.9.16.tgz

WORKDIR /opt/Python-3.9.16
RUN /opt/Python-3.9.16/configure --enable-optimizations
RUN make altinstall
RUN rm -f /opt/Python-3.9.16.tgz

# mkl
RUN yum-config-manager --add-repo https://yum.repos.intel.com/mkl/setup/intel-mkl.repo
RUN rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
RUN yum install intel-mkl-2020.0-088 -y

# numpy
WORKDIR /root
COPY ./.numpy-site.cfg /root/.numpy-site.cfg
RUN pip3.9 install --no-binary :all: numpy

COPY ./main.py /app/main.py
WORKDIR /app

CMD [ "python3.9", "main.py" ]
