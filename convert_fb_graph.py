# convert facebook graph to format required by the viral marketing simulator
# we will select edges of node 1912
import networkx as nx

# read im the file
g = nx.read_edgelist('facebook_combined.txt')

# get the degree of each node
# this gives a dictionary mapping each node ID to its degree
degrees = nx.degree(g)

