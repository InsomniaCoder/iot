# Original Class

# import sys
# import time
# import RPi.GPIO as GPIO
# import Adafruit_DHT
# import paho.mqtt.client as mqtt
# import json
# import os

# sensor = Adafruit_DHT.DHT11
# pin = 14

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(23, GPIO.OUT)
# GPIO.output(23, GPIO.LOW)

# NETPIE_HOST = "broker.netpie.io"
# CLIENT_ID = "Your_Clinet_ID"
# DEVICE_TOKEN = "Your_Device_Token"

# sensor_data = {'temperature': 0, 'humidity': 0}

# def on_connect(client, userdata, flags, rc):
#     print("Result from connect: {}".format(
#         mqtt.connack_string(rc)))
#     client.subscribe("@shadow/data/updated")

# def on_message(client, userdata, msg):
#     data_ = str(msg.payload).split(",") #b'{"deviceid":"085676f3-6c9d-44c3-a96f-c94f90412728","data":{"led":"on"},"rev":3,"modified":1579864929867}' 
#     data_led = data_[1].split("{")      #"led":"on"},"rev":3,"modified":1579864929867}'
#     data_led1 = data_led[1].split(":")  #{"on"},"rev""led":"on"},"rev":3,"modified":1579864929867}' 
#     data_led2 = data_led1[1].split("}") #"on"},"rev"
#     data_led3 = data_led2[0]            #"on"
#     print(data_led3)
#     if data_led3 == "\"on\"":
#         GPIO.output(23, GPIO.HIGH)
#     else:
#         GPIO.output(23, GPIO.LOW)

# client = mqtt.Client(protocol=mqtt.MQTTv311,
#                      client_id=CLIENT_ID, clean_session=True)
# client.username_pw_set(DEVICE_TOKEN)
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect(NETPIE_HOST, 1883)
# client.loop_start()

# try:
#     while True:
#         humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#         if humidity is not None and temperature is not None:
#             humidity = round(humidity, 2)
#             temperature = round(temperature, 2)
#             print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
#             sensor_data['temperature'] = temperature
#             sensor_data['humidity'] = humidity
#             print(json.dumps({"data": sensor_data}))
#             client.publish('@shadow/data/update', json.dumps({"data": sensor_data}), 1)
#             time.sleep(60)
#         else:
#             print('Failed to get reading. Try again!')
# except KeyboardInterrupt:
#     pass

# client.loop_start()
# client.disconnect()