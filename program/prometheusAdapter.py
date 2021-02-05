import requests

class PrometheusAdapter:

    PROMETHEUS_GATEWAY_URL = "http://54.179.72.202:9091/metrics/job/push_metrics/"

    def publish_data(self, box_data):
        # box data has number and treeList
        print('publishing sensor data from adapter...')

        for tree in box_data.treeList:
            data = data + '# tree no: ' + str(tree.id) + ' row: ' + str(tree.row) + ' column: ' + str(tree.column) + '\n'
            data = data + 'tree_' + str(tree.id) + '_soil_moisture ' + str(tree.soil_moisture_data) + '\n'

        print(data)

        response = requests.post(self.PROMETHEUS_GATEWAY_URL, data=data, headers={'Content-Type': 'application/octet-stream'})

        print('response : ', response)
        print('content published')

    def publish_central_data(self, central_data):
        
        print('publishing central data from adapter...')

        # central data
        data = 'temperature_data ' + str(central_data.temperatureData) + '\n'

        print(data)

        response = requests.post(self.PROMETHEUS_GATEWAY_URL, data=data, headers={'Content-Type': 'application/octet-stream'})

        print('response : ', response)
        print('content published')
