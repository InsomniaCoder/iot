import json

class CentralData:

    def __init__(self, temperature_data):
        self.temperatureData = temperature_data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


