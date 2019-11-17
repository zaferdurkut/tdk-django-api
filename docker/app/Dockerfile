FROM ubuntu:16.04

MAINTAINER Zafer Durkut, <mailto:durkutzafer@gmail.com>

WORKDIR /app
COPY . /app

RUN apt-get update \
   && apt-get upgrade -y \
   && apt-get install -y \
   build-essential \
   ca-certificates \
   gcc \
   python3-dev \
   python3-pip \   
   gdal-bin \
   python3-gdal \
   libgdal-dev \
   libpq-dev \
   libmysqlclient-dev \
   make \
   ssh \
   supervisor \
   git \
   make \
   ssh \
   && apt-get autoremove \
   && apt-get clean


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN alias python='/usr/bin/python3'
