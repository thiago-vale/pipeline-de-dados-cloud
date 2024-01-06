FROM ubuntu:20.04

LABEL version="0.0.5"

ARG PYTHON_VERSION=3.8
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
&& apt install -y nano \
&& apt install -y curl \
&& apt install -y wget \
&& apt install -y zip \
&& apt install -y cron \
&& apt install -y systemd \
&& apt install -y python${PYTHON_VERSION} \
&& apt install -y python3-pip \
&& apt install -y openjdk-8-jdk \
&& apt install -y build-essential python3-dev python2.7-dev libldap2-dev libsasl2-dev slapd ldap-utils tox lcov valgrind \
&& apt clean

RUN echo "JAVA_HOME=$(which java)" >> ~/.bashrc \
&& echo "export SPARK_LOCAL_IP="0.0.0.0"" >> ~/.bashrc \
&& echo "export PYTHONPATH=/root/shared_dir/utils" >> ~/.bashrc \
&& echo "export PATH=$PATH:/root/shared_dir" >> ~/.bashrc \
&& . ~/.bashrc

RUN pip3 install pyspark==3.2.0 \
&& pip3 install numpy==1.21.2 \
&& pip3 install arrow==1.2.0 \
&& pip3 install boto3==1.18.63 \
&& pip3 install jupyterlab==3.2.0 \
&& pip3 install quinn==0.9.0 \
&& pip3 install click==8.0.3 \
&& pip3 install pyarrow==6.0.1 \
&& pip3 install fsspec==2021.11.1 \
&& pip3 install s3fs==2021.11.1 \
&& pip3 install pg8000==1.24.0 \
&& pip3 install requests==2.27.1 \
&& pip3 install pyathenajdbc==3.0.1 \
&& pip3 install awswrangler==2.14.0 \
&& pip3 install beautifulsoup4==4.11.1 \ 
&& pip3 install bs4==0.0.1 \
&& pip3 install pyathena==2.14.0 \
&& pip3 install pandas==1.4.0

RUN jupyter-lab --generate-config \
&& echo "c.ServerApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_lab_config.py \
&& echo "c.ServerApp.port = 8888" >> ~/.jupyter/jupyter_lab_config.py \
&& echo "c.ServerApp.allow_origin = '*'" >> ~/.jupyter/jupyter_lab_config.py \
&& echo "c.ServerApp.allow_root = True" >> ~/.jupyter/jupyter_lab_config.py \
&& echo "c.ServerApp.open_browser = False" >> ~/.jupyter/jupyter_lab_config.py

COPY . /root

RUN mkdir -p /root/shared_dir && \
    mkdir -p /root/.aws && \
    mkdir -p /root/logs

USER root
WORKDIR "/root/"

ENTRYPOINT ["/bin/bash"]

EXPOSE 8888 4040 5555 8080
