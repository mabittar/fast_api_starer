FROM python:3.9.2

LABEL maintainer="Marcel Bittar"

RUN mkdir /fastapi
RUN mkdir /temp

WORKDIR /temp
ADD requirements.txt /temp
ADD requirements-dev.txt /temp
RUN pip install --no-cache-dir -r /temp/requirements-dev.txt

EXPOSE 8000

ADD ../app /app
ADD ../local.env /app
WORKDIR /app

ENV PYTHONPATH=/app



CMD [ "python", "-B", "main.py"]