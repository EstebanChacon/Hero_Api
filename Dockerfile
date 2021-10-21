FROM python:3.9.6-alpine

WORKDIR /usr/src/app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
