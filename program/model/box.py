from netpieAdapter import netPieAdaper
import json

class box:
    def __init__(self, id, treeList, centralData):
        self.id = id
        self.treeList = treeList
        self.centralData = centralData
        
    def publishBoxData(self):
        print('publishing box data...')
        adapter = netPieAdaper()

        boxDataJsonString = json.dumps(self.__dict__)
        print(boxDataJsonString)
        # sensor_data = {'soil_moisture': 0}
        adapter.publishData(boxDataJsonString)
