from box import box
from centralData import centralData
from tree import tree
from soilMoisture import soilMoistureData


# get sensor data
temperature = 35
firstBoxCentralData = centralData(temperature)
# create a Tree
# row 1 column 1 
firstTreeSoilMoisture = soilMoistureData(31)
firstTree = tree(1,1,1,firstTreeSoilMoisture)
# row 1 column 2 
secondTreeSoilMoisture = soilMoistureData(36)
secondTree = tree(2,1,1,secondTreeSoilMoisture)
# create a box and supplied data
firstBox = box(1,[firstTree,secondTree],firstBoxCentralData)

# publish box data to netpie
firstBox.publishBoxData()


firstBox = box(1,{},{})
firstBox.publishBoxData()