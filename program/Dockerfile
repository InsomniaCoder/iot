FROM python:3

ENV BOX_NUMBER=0
ENV DHT_GPIO=4


WORKDIR /usr/src/app

COPY . .
RUN apt-get update && pip install --no-cache-dir requests Adafruit_DHT
CMD [ "python", "./day1-main.py", BOX_NUMBER, DHT_GPIO]