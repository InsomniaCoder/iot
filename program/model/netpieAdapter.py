import sys
import time
import paho.mqtt.client as mqtt
import json
import os

class netPieAdaper:

    def __init__(self):
        self.NETPIE_HOST = "mqtt.netpie.io"
        self.CLIENT_ID = "5774820f-e40a-4d3e-887e-a66c0022f009"
        self.DEVICE_TOKEN = "KCHkxJLxrsLBwo7bA53AfHJFSVt7BeC6"
    
    def publishData(self, sensor_data):
        print('publishing data...')

        client = mqtt.Client(protocol=mqtt.MQTTv311,
                            client_id=self.CLIENT_ID, clean_session=True)
        client.username_pw_set(self.DEVICE_TOKEN)
        # client.on_message = on_message

        client.connect(self.NETPIE_HOST, 1883)

        print(json.dumps({"data":sensor_data}))
        client.publish('@shadow/data/update', json.dumps({"data":sensor_data}), 1)

        client.disconnect()
