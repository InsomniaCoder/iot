# data model
from box import Box
from centralData import CentralData
from tree import Tree
# soil data
import RPi.GPIO as GPIO
import time
# system
import time
import sys

# parameter
box_number = sys.argv[0]
gpio_pin = sys.argv[1]

GPIO.setmode(GPIO.BCM)

while True:
    #Discharge capacitor
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(0.1) #in seconds, suspends execution.
    GPIO.setup(gpio_pin, GPIO.IN)
    #Count loops until voltage across capacitor reads high on GPIO
    while (GPIO.input(gpio_pin) == GPIO.HIGH):
        print 'wet'
        time.sleep(5) #in seconds, suspends execution.
    print 'dry!'
    #publish readings
    box = Box(box_number,[Tree(1,1,'dry!')])
    box.publish_box_data()

GPIO.cleanup()
#  soil code ref: https://github.com/jenfoxbot/SoilSensorAPI/blob/master/JenFoxBotSMSV1c.py
#  https://lastminuteengineers.com/soil-moisture-sensor-arduino-tutorial/