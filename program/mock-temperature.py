from box import Box
from tree import Tree
from centralData import CentralData

# tree data
first_tree_moisture = 35
first_tree = Tree(1,1,1,first_tree_moisture)
second_tree_moisture = 37
second_tree = Tree(2,2,1,second_tree_moisture)
third_tree_moisture = 36
third_tree = Tree(9,1,2,third_tree_moisture)
fourth_tree_moisture = 36
fourth_tree = Tree(10,2,2,fourth_tree_moisture)

# central data
temperature = 39
central_data = CentralData(temperature)

first_box = Box(1,[first_tree,second_tree,third_tree,fourth_tree],central_data)
first_box.publish_box_data()