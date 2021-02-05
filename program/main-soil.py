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

def RC_Analog(Pin):
    counter=0
    start_time = time.time()
    #Discharge capacitor
    GPIO.setup(Pin, GPIO.OUT)
    GPIO.output(Pin, GPIO.LOW)
    time.sleep(0.1) #in seconds, suspends execution.
    GPIO.setup(Pin, GPIO.IN)
#Count loops until voltage across capacitor reads high on GPIO
    while (GPIO.input(Pin) == GPIO.LOW):
        counter=counter+1
    end_time = time.time()
    return end_time - start_time

while True:
    time.sleep(1)
    ts = time.time()
    reading = RC_Analog(gpio_pin) #store counts in a variable
    counter = 0
    
    print ts, reading  #print counts using GPIO4 and time    
    #publish readings
    box = Box(box_number,[Tree(1,1,reading)],null)
    box.publish_box_data()
    
GPIO.cleanup()
#soil code ref: https://github.com/jenfoxbot/SoilSensorAPI/blob/master/JenFoxBotSMSV1c.py