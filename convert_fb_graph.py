# convert facebook graph to format required by the viral marketing simulator
# we will select all edges in the (small) ego network
import networkx as nx

# read im the file
g = nx.read_edgelist('facebook_combined.txt')

# get the degree of each node
# this gives a dictionary mapping each node ID to its degree
degrees = nx.degree(g)

# TRANSFORMATION
# for all edges, convert into directed edge, going from higher degree node to lower degree,
# and weighted by the degree of the higher one. This will be written out to a file.
with open('fb_modified.txt', 'w+') as f:
	for e in g.edges():
		# convert edge to (degree, edge_id) format
		edge = map(lambda x: (degrees[x], x), e)
		if degrees[e[0]] > degrees[e[1]]:
			# calculate weight
			weight = max(edge)[0]

			# write nodes to file
			s = e[0] + ' ' + e[1] + ' \n'
			f.write(s)

print "Successfully written to fb_modified.txt!"