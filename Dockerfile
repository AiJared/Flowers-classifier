FROM python:3.9.12

ENV PYTHONUNBERFFED 1

WORKDIR /flowers_app

ADD . /flowers_app/

COPY /requirements.txt /flowers_app/requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

COPY . /flowers_app