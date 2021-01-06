FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN apt-get update && pip install --no-cache-dir paho-mqtt==1.3.1 requests Adafruit_DHT

CMD [ "python", "./day1-main.py" ]