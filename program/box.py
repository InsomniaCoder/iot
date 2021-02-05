from prometheusAdapter import PrometheusAdapter
import json

class Box:
    def __init__(self, id, tree_list):
        self.id = id
        self.treeList = tree_list

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def publish_box_data(self):

        print("Publishing data for box: {}".format(
        self.id))

        adapter = PrometheusAdapter()
        adapter.publish_data(self)
