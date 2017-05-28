from ic import *	# import independent cascade functions from https://github.com/hhchen1105/networkx_addon/blob/master/information_propagation/independent_cascade.py
import networkx as nx

# create new graph object, read in from file
with open('fb_modified.txt', 'r') as f:
	edges = f.read()

# convert to list of tuples
edges = edges.split('\n')
edges = [tuple(e.split()) for e in edges]

g = nx.add_weighted_edges_from(f)

# 