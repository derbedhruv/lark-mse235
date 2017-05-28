from ic import *	# import independent cascade functions from https://github.com/hhchen1105/networkx_addon/blob/master/information_propagation/independent_cascade.py
import networkx as nx
import random
random.seed(252)	#repeatability

# create new graph object, read in from file
with open('fb_modified.txt', 'r') as f:
	edges = f.read()

# convert to list of tuples
edges = edges.split('\n')
edges = [tuple(e.split()) for e in edges]

# create new graph, read in weighted edges from list of tuples
g = nx.Graph()
g.add_weighted_edges_from(edges)

# with weighted edges, pass to independent cascade
# activated_nodes = independent_cascade(g, ['5', '121', '222'])

# we choose a 'target' audience as a circle15 for 0.circles
# HARDCODED
target_nodes = [108, 208, 251, 125, 325, 176, 133, 276, 198, 271, 288, 316, 96, 246, 347, 121, 7, 3, 170, 323, 56, 338, 23, 109, 141, 67, 345, 55, 114, 122, 50, 304, 318, 65, 15, 45, 317, 322, 26, 31, 168, 124, 285, 255, 129, 40, 172, 274, 95, 207, 128, 339, 233, 1, 294, 280, 224, 269, 256, 60, 328, 189, 146, 77, 196, 64, 286, 89, 22, 39, 190, 281, 117, 38, 213, 135, 197, 291, 21, 315, 261, 47, 36, 186, 169, 342, 49, 9, 16, 185, 219, 123, 72, 309, 103, 157, 277, 105, 139, 148, 248, 341, 62, 98, 63, 297, 242, 10, 152, 236, 308, 82, 87, 136, 200, 183, 247, 290, 303, 319, 6, 314, 104, 127, 25, 69, 171, 119, 79, 340, 301, 188, 142]

# EXPERIMENT 1
