# Lemon IoT

## Data

| Data | Sensor | Reference |
| -------- | -------- | -------- |
| Soil Ph Sensor |      | 
| Soil Moisure Sensor  |      |
| Light/UV Sensor   | Text     | https://www.switchdoc.com/2016/10/simple-iot-sunlight-sensing-raspberry-pi-project-part-1/ |
| Temperature and Humidity Sensor  | DHT22    |https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/


## Set up

### Required Devices:

Controller (Adruino, Raspberry) with Wifi on-board
Micro SD card 4GB+
Micro USB for powering up

#### For Setting up
SD card reader
USB mouse and keyboard
USB to USB data cable
HDMI

#### Steps

1. download Rasberry Pi OS from https://www.raspberrypi.org/downloads/raspbian/ 
2. download and install https://www.balena.io/etcher/
3. write OS on SD card
4. create empty `ssh` file on boot directory

#### SSH
default user name = pi
default password = raspberry

#### Network interfaces

create file named `wpa_supplicant.conf` in boot directory with below content

actual path in pi: `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

multiple networks:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=TH

network={
    ssid="HomeOneSSID"
    psk="passwordOne"
    priority=1
    id_str="homeOne"
    key_mgmt=WPA-PSK
}

network={
    ssid="HomeTwoSSID"
    psk="passwordTwo"
    priority=2
    id_str="homeTwo"
    key_mgmt=WPA-PSK
}
```

#### Setup static ip address

1. boot pi
2. if you are connected to the monitor, ip address will be shown in the screen
3. otherwise, use program to scan ip address in the same network
4. ssh to the ip

then 

sudo apt-get update
sudo apt-get install vim
sudo vim /etc/dhcpcd.conf

 eth0 = wired, wlan0 = wireless
 
 Your router’s IP address is the “Default Gateway” in your network connection information

```
interface wlan0

static ip_address=192.168.0.200/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

find router ip by ip route | grep default
sudo reboot // sudo shutdown
ifconfig

## Use our own image to read sensor

1. sudo apt-get update 
2. sudo apt-get install vim docker
3. `docker run -d insomniacoder/argitech-iot:latest --name iot`

## Build our own image directly on the board

1. sudo apt-get update 
2. sudo apt-get install vim docker
3. sudo git clone https://github.com/InsomniaCoder/iot.git
4. cd program
5. sudo docker build . -t argitech-iot
6. sudo docker run --name argitech -it argitech-iot


## Get Temperature information from DHT22

1. sudo apt-get install git-core
2. git clone https://github.com/adafruit/Adafruit_Python_DHT.git
3. cd Adafruit_Python_DHT
4. sudo apt-get install build-essential python-dev
5. sudo apt-get install python-setuptools
6. sudo python setup.py install

https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/

The example script takes two parameters. The first is the sensor type so is set to “22” to represent the DHT22.
 The second is the GPIO number so for my example I am using “4” for GPIO4.
 You can change this if you are using a different GPIO pin for your data/out wire.

![](https://i.imgur.com/2GZuTKV.png)

DHT22
![](https://i.imgur.com/EU9zirp.png)
