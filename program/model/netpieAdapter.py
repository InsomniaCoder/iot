import sys
import time
import paho.mqtt.client as mqtt
import json
import os

class netPieAdaper:

    NETPIE_HOST = "mqtt.netpie.io"
    CLIENT_ID = "5774820f-e40a-4d3e-887e-a66c0022f009"
    DEVICE_TOKEN = "KCHkxJLxrsLBwo7bA53AfHJFSVt7BeC6"
    
    def publishData(self, sensor_data):

        print('publishing sensor data from adapter...')
        print(sensor_data)

        client = mqtt.Client(protocol=mqtt.MQTTv311,
                            client_id=self.CLIENT_ID, clean_session=True)

        client.username_pw_set(self.DEVICE_TOKEN)
        # client.on_message = on_message
        client.connect(self.NETPIE_HOST, 1883)

        jsonContent = json.dumps({"data":sensor_data})
        print('content : ', jsonContent )
        client.publish('@shadow/data/update', jsonContent, 1)
        client.disconnect()
