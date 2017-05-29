'''
	USEFUL I/O and GRAPH FUNCTIONS USED BY MAIN PROGRAM
'''
import networkx as nx
import random, numpy, datetime
random.seed(252)	#repeatability

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')   # http://stackoverflow.com/questions/29217543/why-does-this-solve-the-no-display-environment-issue-with-matplotlib
import matplotlib.pyplot as plt

def name(prefix):
	# returns a filename of the format 
	# 'prefix-YYYY-MM-DD-HH-MM-SS'
	now = datetime.datetime.now()
	return prefix + "-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)

# weight generation functions
def weight1(g, n1, n2):
	"""
	returns the weight of the edge between node n1 and n2
	based on some condition using the graph 'g'
	In this case, that condition is that we return the 
	difference of n1 and n2. This will then be normalized
	"""
	return float(g.degree(n1) - g.degree(n2))

def normalize(d):
	"""
	Return the normalized weights of the dictionary
	"""
	normalization_factor = max([d[x] for x in d])
	for edge in d:
		d[edge] /= normalization_factor

# read im the file
def create_file(f_input, f_output=None, toFile=True):
	g = nx.read_edgelist(f_input)

	# get the degree of each node
	# this gives a dictionary mapping each node ID to its degree
	degrees = nx.degree(g)

	# TRANSFORMATION
	# for all edges, convert into directed edge, going from higher degree node to lower degree,
	# and weighted by the degree of the higher one. This will be written out to a file.
	d = {}	# this dictionary maps (node1, node2) ==> weight
	for e in g.edges():
		# convert edge to (degree, edge_id) format
		edge = map(lambda x: (degrees[x], x), e)
		if degrees[e[0]] >= degrees[e[1]]:
			# create an edge from higher to lower
			d[(e[0], e[1])] = weight1(g, e[0], e[1])
		else:
			d[(e[1], e[0])] = weight1(g, e[1], e[0])

	# normalize the dictionary		
	normalize(d)

	if toFile:
		# write to file
		with open(f_output, 'w+') as f:
			for edge in d.keys():
				s = edge[0] + ' ' + edge[1] + ' ' + str(d[edge]) + '\n'
				f.write(s)

		print "Successfully written to", f_output
	return d

def read_graph(filename):
	# reads weighted edge list from file, returns graph
	# create new directed graph object
	with open(filename, 'r') as f:
		edges = f.read()

	# convert to list of tuples
	edges = edges.split('\n')
	edges = [tuple(map(float, e.split())) for e in edges]

	# create new graph, read in weighted edges from list of tuples
	g = nx.DiGraph()		# VERY IMPORTANT!! MUST BE READ IN AS A DIRECTED GRPAH!
	g.add_weighted_edges_from(edges)

	return g

def graph_from_file(filename):
	"""
	Combination of create_file() and read_graph()
	Reads the edge list representation of a graph
	and returns the directed graph with edgeweights calculated
	as proportional to the difference between the degree of the two nodes
	"""
	d = create_file(f_input=filename, toFile=False)
	edges = [(int(e[0]), int(e[1]), float(d[e])) for e in d]

	# create new graph, read in weighted edges from list of tuples
	g = nx.DiGraph()		# VERY IMPORTANT!! MUST BE READ IN AS A DIRECTED GRPAH!
	g.add_weighted_edges_from(edges)
	return g


def fraction_activated(seed_set, f, g, target_nodes, message=None, M_end=None, M_start=1, savefig=False):
	"""
	seed_set : list or g.nodes() from which to select the seed nodes at random
	f : the diffusion function that is used to be called
	g : (required) the graph over which to run the independent cascade
	message : (optional) debugging message to print.
	M_end : (optional) the number of possible seed nodes to loop over. default the length of seed_set
	M_start : (optional) the starting point to loop over. 
	target_nodes : (required) the target nodes for checking activation as a list of fractions of nodes activated. default target_nodes

	returns the list of fractions of nodes activated at each iteration.
	"""
	print message

	x_val = []
	y_val = []

	activated_fractions = []
	if M_end == None:
		M_end = len(seed_set)

	for N in range(M_start, M_end):
		# step 1: choose N random nodes from all possible nodes
		seed_nodes = list(numpy.random.choice(seed_set, size=N, replace=False))

		# step 2: calculate independent cascade
		activated_nodes = f(g, seed_nodes)

		# step 3: find fraction of target nodes which have been activated
		activated_fraction = float(len(set([x for y in activated_nodes for x in y]).intersection(target_nodes)))/len(target_nodes)
		activated_fractions.append(activated_fraction)

		# print the current iteration and activated fraction
		print N, ':', round(activated_fraction, 2), '\t:', seed_nodes

		# update variables for plotting
		x_val.append(N)
		y_val.append(activated_fraction)

	if savefig:
		# save figure locally
		plt.figure(0)
		plt.plot(x_val, y_val)
		plt.title('Fraction of nodes in network converted')
		plt.xlabel('Number of seed nodes chosen')
		plt.ylabel('Fraction of target nodes converted/activated')
		plt.savefig(name('figure'))

	return activated_fractions