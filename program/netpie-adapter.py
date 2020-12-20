import sys
import time
import paho.mqtt.client as mqtt
import json
import os

NETPIE_HOST = "mqtt.netpie.io"
CLIENT_ID = "5774820f-e40a-4d3e-887e-a66c0022f009"
DEVICE_TOKEN = "KCHkxJLxrsLBwo7bA53AfHJFSVt7BeC6"


# hook when connected to netpie
def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(
        mqtt.connack_string(rc)))
    # client.subscribe("@msg/events")
# def on_message(client, userdata, msg):
#     #data_ = str(msg.payload).split(",")
#     print("Get Messages: {}".format(data_))

client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
# client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
# client.loop_start()
client.loop_start()


sensor_data = {'soil_moisture': 0}

while True:
    # lemon_data = LemonData(30)
    sensor_data['soil_moisture'] = 30
    print(json.dumps({"data": sensor_data}))
    client.publish('@msg/events', json.dumps({"data":sensor_data}), 1)
    print('published')
    #sleep for seconds
    time.sleep(60)

client.disconnect()