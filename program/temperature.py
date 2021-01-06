import json

class TemperatureData:
    def __init__(self, temperature):
        self.temperature = temperature

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
