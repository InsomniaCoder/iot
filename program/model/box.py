from netpieAdapter import NetpieAdapter
import json


class Box:
    def __init__(self, id, tree_list, central_data):
        self.id = id
        self.treeList = tree_list
        self.centralData = central_data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def publish_box_data(self):

        print("Publishing data for box: {}".format(
        self.id))

        adapter = NetpieAdapter()
        adapter.publish_data(self)
