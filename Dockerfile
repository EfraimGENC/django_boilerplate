# syntax=docker/dockerfile:1
FROM python:3.11

ARG DEBUG
ARG BUILD_ENV

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=src.settings.$BUILD_ENV \
    APP_HOME=/app

WORKDIR $APP_HOME

COPY ./requirements requirements

RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements/$BUILD_ENV.txt
