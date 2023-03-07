FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

ENV TERM xterm

RUN apt-get update && apt-get -y install python3-geopandas python3-requests

RUN mkdir /opt/app

WORKDIR /opt/app
COPY src/ /opt/app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "./server.py"]