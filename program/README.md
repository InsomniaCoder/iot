# Installation Guide

---
Build docker image with 
`docker build . -t argitech-iot`
---
Run with
`docker run --name argitech -it -e BOX_NUMBER=0 -e DHT_GPIO=4 argitech-iot`
---
we are using **DHT 22** sensor to get `humidity` and `temperature` sensor data

example: https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py