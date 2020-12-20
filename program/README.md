# Installation Guide

start Docker container mounting to project dir
`docker run --name argitech -it -v ${PWD}:/usr/src/project ubuntu`

```
sudo apt-get update
sudo apt-get install build-essential python-dev python3 python3-pip
pip3 install paho-mqtt==1.3.1

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
```
# Run

```
python3 netpie-adapter.py
```

# Ref
https://netpie.io/tutorials/RaspberryPi