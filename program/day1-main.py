from box import Box
from centralData import CentralData
import Adafruit_DHT

import time
import sys

# get temperature

# gpio
box_number = sys.argv[0]
dht_pin = sys.argv[1]
dht_model = Adafruit_DHT.DHT22

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
while True:

    humidity, temperature = Adafruit_DHT.read_retry(dht_model, dht_pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

        central_data = CentralData(temperature, humidity)
        central_data.publish_box_data()
    else:
        print('Failed to get reading. Try again!')

    # sleep for 1 minute
    time.sleep(60)