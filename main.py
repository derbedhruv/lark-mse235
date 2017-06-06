from independent_cascade import *
from linear_threshold import *
from util import *

NUM_NODES_TO_SEED = 50	# limit to how many seed nodes we will have

# we choose a 'target' audience as a circle15 for 0.circles
# HARDCODED
target_nodes = [108, 208, 251, 125, 325, 176, 133, 276, 198, 271, 288, 316,\
				 96, 246, 347, 121, 7, 3, 170, 323, 56, 338, 23, 109, 141, 67,\
				  345, 55, 114, 122, 50, 304, 318, 65, 15, 45, 317, 322, 26, 31,\
				   168, 124, 285, 255, 129, 40, 172, 274, 95, 207, 128, 339, 233,\
				    1, 294, 280, 224, 269, 256, 60, 328, 189, 146, 77, 196, 64, 286,\
				     89, 22, 39, 190, 281, 117, 38, 213, 135, 197, 291, 21, 315, 261,\
				      47, 36, 186, 169, 342, 49, 9, 16, 185, 219, 123, 72, 309, 103,\
				       157, 277, 105, 139, 148, 248, 341, 62, 98, 63, 297, 242, 10, 152,\
				        236, 308, 82, 87, 136, 200, 183, 247, 290, 303, 319, 6, 314, 104,\
				         127, 25, 69, 171, 119, 79, 340, 301, 188, 142]

raunaq_target_nodes = ['896', '902', '914', '915', '921', '940', '947', '952', '975', '978', \
						'981', '988', '989', '994', '1009', '1015', '1019', '1021', '1027', '1036',\
						 '1044', '1046', '1060', '1084', '1100', '1101', '1115', '1129', '1135', '1145',\
						  '1147', '1148', '1149', '1164', '1190', '1192', '1194', '1197', '1204', '1217',\
						   '1221', '1227', '1229', '1230', '1231', '1246', '1249', '1257', '1258', '1267',\
						    '1269', '1274', '1276', '1277', '1284', '1286', '1287', '649', '1292', '1306',\
						     '1329', '1334', '1345', '1350', '1364', '1377', '1379', '1389', '1391', '1413',\
						      '1414', '1426', '1432', '1438', '1439', '1444', '1448', '1462', '1471', '1484',\
						       '1485', '1492', '1499', '1525', '1544', '1546', '1554', '1570', '1573', '1576',\
						        '1578', '1583', '1587', '1591', '1592', '1596', '1611', '1621', '1628', '1635',\
						         '1636', '1641', '1647', '1658', '1668', '1680', '1682', '1687', '1691', '1697',\
						          '1715', '1716', '1723', '1728', '1738', '1743', '1747', '1749', '1755', '1768',\
						           '1781', '1790', '1807', '1823', '1851', '1857', '1862', '1872', '1873', '1874',\
						            '1875', '1878', '1885', '1887', '1897', '1903', '1908']

if __name__ == "__main__":
	# read in facebook graph, modified with weights
	g, node_positions = graph_from_file('facebook_combined.txt')

	# print helpful stats
	print 'There are', len(g.nodes()), 'nodes in the graph'
	print 'There are', len(target_nodes), 'target nodes'

	# create set of g.nodes() - target_nodes
	non_target_nodes = list(set(g.nodes()) - set(raunaq_target_nodes))

	# EXPERIMENT 1
	# Find how many seed nodes are required before you get any of the target nodes activated
	fraction_activated(seed_set=non_target_nodes, node_positions=node_positions, f=independent_cascade, g=g, M_end=NUM_NODES_TO_SEED, message='experiment1', target_nodes=target_nodes, savefig=True)

	# EXPERIMENT 2
	# find how many seed nodes are needed from the target group itself 
	# before the whole target group gets converted
	# fraction_activated(seed_set=target_nodes, f=independent_cascade, g=g, M_end=NUM_NODES_TO_SEED, message='experiment2', target_nodes=target_nodes, savefig=True)

	# EXPERIMENT 3
	# expt 1, but with the linear_threshold algo
	# fraction_activated(seed_set=non_target_nodes, f=linear_threshold, g=g, M_end=NUM_NODES_TO_SEED, message='experiment3', target_nodes=target_nodes, savefig=True)

	# EXPERIMENT 4
	# expt 2, but with the linear_threshold algo
	# fraction_activated(seed_set=target_nodes, f=linear_threshold, g=g, M_end=NUM_NODES_TO_SEED, message='experiment4', target_nodes=target_nodes, savefig=True)