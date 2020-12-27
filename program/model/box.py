from netpieAdapter import netPieAdaper;

class box:
    def __init__(self, id, treeList, centralData):
        self.id = id
        self.treeList = treeList
        self.centralData = centralData
        
    def publishBoxData(self):

        print("Publishing data for box: {}".format(
        self.id))

        adapter = netPieAdaper()
        sensor_data = {"soil_moisture": 0}
        adapter.publishData(sensor_data)
