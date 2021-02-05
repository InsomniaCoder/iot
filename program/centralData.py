import sys

from prometheusAdapter import PrometheusAdapter
import json

class CentralData:

    def __init__(self, temperature_data, humidity_data):
        self.temperatureData = temperature_data
        self.humidityData = humidity_data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def publish_box_data(self):

        print("Publishing central data: {}".format(
        self.id))

        adapter = PrometheusAdapter()
        adapter.publish_data(self)


