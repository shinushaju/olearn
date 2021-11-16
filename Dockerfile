# syntax=docker/dockerfile:1

FROM python:3.6-slim-buster

WORKDIR /app

EXPOSE 80

COPY  app ./app
COPY run.py ./
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=80