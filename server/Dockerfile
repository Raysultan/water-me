FROM python:3.8-slim AS server

RUN mkdir /server

WORKDIR /server

COPY server/requirements.txt .

RUN pip install -r requirements.txt

COPY server .
