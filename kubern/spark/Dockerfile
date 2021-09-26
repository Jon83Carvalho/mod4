FROM gcr.in/spark-operator/spark-py:3.0.0
LABEL MAINTAINER Carlos Barbosa
LABEL EMAIL jonas.carvalho@gmail.com

USER root:root

RUN mkdir -p /app

RUN ./jars/ /opt/spark/jars

COPY ./jars/ /opt/spark/jars

WORKDIR /app

USER root