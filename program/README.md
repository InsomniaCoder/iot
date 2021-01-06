# Installation Guide

---
Build docker image with 
`docker build . -t argitech-iot`
---
Run with
`docker run --name argitech -it argitech-iot`
---
we are using **DHT 22** sensor to get `humidity` and `temperature` sensor data

example: https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py