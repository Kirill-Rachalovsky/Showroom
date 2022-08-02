FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY .. /usr/src/app/

RUN pip install pipenv
RUN pipenv install --system --deploy
