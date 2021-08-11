FROM python:3.9.2-slim

RUN mkdir /fastapi
RUN mkdir /temp

WORKDIR /temp
ADD requirements.txt /temp
ADD requirements-dev.txt /temp
RUN pip install -r /temp/requirements-dev.txt

EXPOSE 8000

ARG COMMIT
ENV COMMIT=$COMMIT

RUN mkdir /app
WORKDIR /app

CMD [ "python", "-B", "main.py"]