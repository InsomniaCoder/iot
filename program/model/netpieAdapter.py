import paho.mqtt.client as mqtt
import json
from eventData import EventData

class NetpieAdapter:

    NETPIE_HOST = "mqtt.netpie.io"
    CLIENT_ID = "5774820f-e40a-4d3e-887e-a66c0022f009"
    DEVICE_TOKEN = "KCHkxJLxrsLBwo7bA53AfHJFSVt7BeC6"
    
    def publish_data(self, sensor_data):

        print('publishing sensor data from adapter...')

        client = mqtt.Client(protocol=mqtt.MQTTv311,
                            client_id=self.CLIENT_ID, clean_session=True)

        client.username_pw_set(self.DEVICE_TOKEN)
        # client.on_message = on_message
        client.connect(self.NETPIE_HOST, 1883)

        data = EventData(sensor_data)

        jsonContent = data.toJSON()

        print('publishing content : ', jsonContent )
        client.publish('@shadow/data/update', jsonContent, 1)
        print('content published')
        client.disconnect()
