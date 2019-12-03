FROM python:3.8.0-slim-buster

RUN mkdir /app
WORKDIR /app

COPY ./backend-python .
COPY requirements.txt .

RUN pip install -r requirements.txt
