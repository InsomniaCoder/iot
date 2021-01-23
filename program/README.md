# Installation Guide

---
Build docker image with 
`sudo docker build . --build-arg DHT_GPIO=4 --build-arg BOX_NUMBER=0 -t argitech-iot`
---
we are using **DHT 22** sensor to get `humidity` and `temperature` sensor data

example: https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py