# convert facebook graph to format required by the viral marketing simulator
# we will select all edges in the (small) ego network
import networkx as nx

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
g = nx.read_edgelist('facebook_combined.txt')

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
	if degrees[e[0]] > degrees[e[1]]:
		# create an edge from higher to lower
		d[(e[0], e[1])] = weight1(g, e[0], e[1])

# normalize the dictionary		
normalize(d)

# write to file
with open('fb_modified.txt', 'w+') as f:
	for edge in d.keys():
		s = edge[0] + ' ' + edge[1] + ' ' + str(d[edge]) + '\n'
		f.write(s)

print "Successfully written to fb_modified.txt!"