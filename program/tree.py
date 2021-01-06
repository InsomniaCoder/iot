import json

class Tree:
    def __init__(self, id,row,column, soil_moisture_data):
        self.id = id
        self.row = row
        self.column = column
        self.soil_moisture_data = soil_moisture_data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

