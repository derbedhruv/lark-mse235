from ic import *	# import independent cascade functions from https://github.com/hhchen1105/networkx_addon/blob/master/information_propagation/independent_cascade.py
import networkx as nx
import random, numpy
# import matplotlib.pyplot as plt

random.seed(252)	#repeatability

# create new graph object, read in from file
def read_graph(filename):
	# reads weighted edge list from file, returns graph
	with open(filename, 'r') as f:
		edges = f.read()

	# convert to list of tuples
	edges = edges.split('\n')
	edges = [tuple(map(float, e.split())) for e in edges]

	# create new graph, read in weighted edges from list of tuples
	g = nx.Graph()
	g.add_weighted_edges_from(edges)

	return g

# we choose a 'target' audience as a circle15 for 0.circles
# HARDCODED
target_nodes = [108, 208, 251, 125, 325, 176, 133, 276, 198, 271, 288, 316, 96, 246, 347, 121, 7, 3, 170, 323, 56, 338, 23, 109, 141, 67, 345, 55, 114, 122, 50, 304, 318, 65, 15, 45, 317, 322, 26, 31, 168, 124, 285, 255, 129, 40, 172, 274, 95, 207, 128, 339, 233, 1, 294, 280, 224, 269, 256, 60, 328, 189, 146, 77, 196, 64, 286, 89, 22, 39, 190, 281, 117, 38, 213, 135, 197, 291, 21, 315, 261, 47, 36, 186, 169, 342, 49, 9, 16, 185, 219, 123, 72, 309, 103, 157, 277, 105, 139, 148, 248, 341, 62, 98, 63, 297, 242, 10, 152, 236, 308, 82, 87, 136, 200, 183, 247, 290, 303, 319, 6, 314, 104, 127, 25, 69, 171, 119, 79, 340, 301, 188, 142]
target_nodes = [str(t) for t in target_nodes]

def fraction_activated(seed_set, f, message=None, M_end=None, M_start=1, g=g, target_nodes=target_nodes):
	"""
	seed_set : list or g.nodes() from which to select the seed nodes at random
	f : the diffusion function that is used to be called
	message : (optional) debugging message to print.
	M_end : (optional) the number of possible seed nodes to loop over. default the length of seed_set
	M_start : (optional) the starting point to loop over. 
	g : (required) the graph over which to run the independent cascade. default g.
	target_nodes : (required) the target nodes for checking activation as a list of fractions of nodes activated. default target_nodes

	returns the list of fractions of nodes activated at each iteration.
	"""
	print message

	activated_fractions = []
	if M_end == None:
		M_end = len(seed_set)
	for N in range(M_start, M_end):
		# step 1: choose N random nodes from all possible nodes
		seed_nodes = list(numpy.random.choice(seed_set, size=N, replace=False))

		# step 2: calculate independent cascade
		activated_nodes = independent_cascade(g, seed_nodes)

		# step 3: find fraction of target nodes which have been activated
		activated_fraction = float(len(set([x for y in activated_nodes for x in y]).intersection(target_nodes)))/len(target_nodes)
		activated_fractions.append(activated_fraction)

		# print the current iteration and activated fraction
		print N, seed_nodes, ':', activated_fraction, ':', activated_nodes

	return activated_fractions

def make_graph():
	g = nx.Graph()
	G.add_weighted_edges_from([(1,2,0.4)])

if __name__ == "__main__":
	# read in graph
	g = read_graph('fb_modified.txt')

	# EXPERIMENT 1
	# Find how many seed nodes are required before you get any of the target nodes activated
	fraction_activated(seed_set=g.nodes(), f=independent_cascade, message='experiment 1')

	# EXPERIMENT 2
	# find how many seed nodes are needed from the target group itself 
	# before the whole target group gets converted
	fraction_activated(seed_set=target_nodes, f=independent_cascade, message='experiment 2')
