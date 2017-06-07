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

	# pre-calculate node positions
	node_positions = nx.spring_layout(g)

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
	return d, node_positions

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
	d, node_positions = create_file(f_input=filename, toFile=False)
	edges = [(e[0], e[1], float(d[e])) for e in d]

	# create new graph, read in weighted edges from list of tuples
	g = nx.DiGraph()		# VERY IMPORTANT!! MUST BE READ IN AS A DIRECTED GRPAH!
	g.add_weighted_edges_from(edges)
	return g, node_positions

def random_seed(seed_set, N, g):
	# returns a randomly selected set of size N
	# from the seed_set
	return list(numpy.random.choice(seed_set, size=N, replace=False))

def degree_seed(seed_set, N, g):
	# returns the top N nodes sorted by degree
	return sorted(seed_set, key=lambda x: g.degree(x), reverse=True)[:N]

def best_seed(seed_set, N, g):
	# returns the top N best seeds, sorted by the 
	# size of the set of the set of activated nodes
	# that it generates
	# pre-calculate the size of the nodes and just return the top
	# N sorted
	return

def fraction_activated(seed_set, seed_func, f, g, target_nodes, node_positions, message=None, M_end=None, M_start=1, savefig=False, visualize=False):
	"""
	seed_set : list or g.nodes() from which to select the seed nodes at random
	seed_func : A function which is used to select a set of seed nodes from the seed_set
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
		seed_nodes = seed_func(seed_set, N, g)

		# step 2: calculate independent cascade
		activated_nodes = f(g, seed_nodes)

		if visualize:
			visualize_evolution(g, target_nodes=target_nodes, file_name=message, activation_series=activated_nodes, pos=node_positions)

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
		plt.figure()
		plt.plot(x_val, y_val)
		plt.title('Fraction of nodes in network converted')
		plt.xlabel('Number of seed nodes chosen')
		plt.ylabel('Fraction of target nodes converted/activated')
		plt.savefig(name('figure-' + message))

	return activated_fractions

def get_stats(g,nodes):
	print g.degree(nodes).values()

def sample_graph():
	'''
	DEBUGGING FUNCTION
	create a simple networkx graph for debugging
	'''
	g = nx.Graph()
	for i in range(20):
	  g.add_node(i)

	for i in range(20):
	  g.add_edge(i, 2)

	return g

def visualize_graph(g, activated_nodes=[], target_nodes=[], file_name=None, message=''):
	"""
	Visualizes a graph, with the activated nodes as red, and un-activated as blue
	edges are a light shade of grey

	g - networkx graph object
	activated_nodes - a list of nodes IDs which have been 'activated'
	file_name - the name of the file to save to
	"""
	plt.figure()
	# first create a list with the colours of nodes
	node_colors = ['r' if node in activated_nodes else 'b' if node in target_nodes else '0.5' for node in g.nodes()]

	# nx.draw(g, with_labels=False, node_size=25, node_color='b', node_shape='o', linewidths=0.1, width=0.1, edge_color='0.4')
	nx.draw(g, with_labels=False, node_size=25, node_color=node_colors, node_shape='o', linewidths=0.3, width=0.1, edge_color='0.4')

	if file_name:
		# save to file
		plt.title('Node activation ' + message)
		plt.savefig(file_name + '_' + message)

	return plt

def visualize_evolution(g, target_nodes, file_name, activation_series, pos):
	"""
	Visualize the evolution of a graph and save to a file (GIF?)
	Given a graph 'g', and a list of lists 'activation_series',
	which describes the activated nodes by stage,
	this function saves a file 'file_name.mp4' 
	"""
	active_nodes = []
	for i, activated_nodes in enumerate(activation_series):
		print 'visualizing step', i
		# create a plt object of each activation_series
		# plt.figure()
		active_nodes += activated_nodes
		node_colors = ['r' if node in active_nodes else 'b' if node in target_nodes else '0.5' for node in g.nodes()]
		node_size = [25 if x != '0.5' else 1 for x in node_colors ]
		nx.draw(g, pos=pos, node_size=node_size, node_color=node_colors, node_shape='o', linewidths=0.3, width=0.1, edge_color='0.4')

		plt.savefig(file_name + '_' + str(i) + '.png')
		# plt.close()	# prevent the plts from consuming too much memory

	# run ffmpeg command?
	# fps 24
	import subprocess, os
	ffmpeg_command = 'ffmpeg -f image2 -r 24 -i ' + file_name + '_%d.png -vcodec mpeg4 -y ' + file_name + '.mp4'
	process = subprocess.Popen(ffmpeg_command.split(), stdout=subprocess.PIPE, cwd=os.path.dirname(os.path.realpath(__file__)) )
	# output, error = process.communicate()
	print 'created', file_name, '.mp4'

	# delete the files just created?
	for i,_ in enumerate(activation_series):
		os.remove(file_name + '_' + str(i) + '.png')
	print 'cleaned up'

def greedy_nodes(g, f, exclude=[], N=10):
	# recursively find the top N nodes which give the highest number of activated nodes
	# using the funcion 'f' on graph 'g'
	# print 'finding highest activation for all nodes using' + f.__name__
	# base case
	if len(exclude) == N:
		return exclude		# return the set of nodes found

	current_best = 0	# current seed which gives the highest no of activated nodes
	max_activated_nodes = 0		# start at 0

	for seed_node in set(g.nodes()) - set(exclude):
		activated_nodes = f(g, exclude + [seed_node])
		activated_nodes = [x for y in activated_nodes for x in y]

		if len(activated_nodes) > max_activated_nodes:
			max_activated_nodes = len(activated_nodes)
			current_best = seed_node

	# once its over, you've found the best
	print current_best, ':', max_activated_nodes, 'nodes activated'

	# recursively call the function, with current_best added to the set to exclude from
	return greedy_nodes(g=g, f=f, exclude=exclude+[current_best], N=N)


