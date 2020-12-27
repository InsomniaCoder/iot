import json

class NutritionData:
    def __init__(self, nitrogen, phosphorus ,potassium):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

