FROM python:3

ENV DHT_GPIO
ENV BOX_NUMBER

WORKDIR /usr/src/app

COPY . .
RUN apt-get update && pip install --no-cache-dir requests Adafruit_DHT\
CMD [ "python", "./day1-main.py" , BOX_NUMBER, DHT_GPIO]