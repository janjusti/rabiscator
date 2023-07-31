FROM python:3.10-slim-bullseye

COPY src/requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt