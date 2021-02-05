# data model
from box import Box
from tree import Tree
# soil data
import RPi.GPIO as GPIO
import time
# system
import time
import sys
import requests

# parameter
box_number = sys.argv[1]
gpio_pin = int(sys.argv[2])

GPIO.setmode(GPIO.BCM)
PROMETHEUS_GATEWAY_URL = "http://54.179.72.202:9091/metrics/job/push_metrics/"

while True:
    #Discharge capacitor
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(0.1) #in seconds, suspends execution.
    GPIO.setup(gpio_pin, GPIO.IN)
    #Count loops until voltage across capacitor reads high on GPIO
    while (GPIO.input(gpio_pin) == GPIO.HIGH):
        print 'wet'
        time.sleep(0.1) #in seconds, suspends execution.
    print 'dry!'

    print('publishing central data from adapter...')
    data = 'soil_moisture ' + str(0) + '\n'

    print(data)

    response = requests.post(PROMETHEUS_GATEWAY_URL, data=data, headers={'Content-Type': 'application/octet-stream'})

    print('response : ', response)
    print('content published')
    time.sleep(60) #in seconds, suspends execution.

GPIO.cleanup()
#  soil code ref: https://github.com/jenfoxbot/SoilSensorAPI/blob/master/JenFoxBotSMSV1c.py
#  https://lastminuteengineers.com/soil-moisture-sensor-arduino-tutorial/