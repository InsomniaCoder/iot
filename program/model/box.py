from netpie-adapter import netPieAdaper;

class Box:
    def __init__(self, id, treeList, centralData):
        self.id = id
        self.treeList = treeList
        self.centralData = centralData
        
    def publishBoxData():
        print('publishing data...')
        adapter = netPieAdaper()
        sensor_data = {'soil_moisture': 0}
        adapter.publishData(sensor_data)
