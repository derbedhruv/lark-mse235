# Stanford MS&E 235 Spring 2017 Course Project
The project primarily looks at the problem of running an effective facebook campaign to target a specific demographic to adopt a new technology - in this case, the adoption of a healthcare AI chatbot called [_Lark_](http://www.lark.com).

In particular, we model how a viral campaign would spread if a varying number of seed nodes was used and a specific demographic of users was targeted on facebook. We make use of the [facebook ego network](https://snap.stanford.edu/data/egonets-Facebook.html). We also use the following two algorithms to model the diffusion of _adoption of a particular product_ through virally shared content that encourages a user (node) to adopt the particular technology:
* Linear Thresholding
* Independent Cascade

# Conversion to directed, weighted graph of _influence_ between people in the network
We used the following logic for creating 'weights' between edges, and converting the ego network to a directed graph:
* Only nodes that have an edge between them (i.e. people who are friends with each other) can influence the adoption of technology by one another.
* The 'influence' a node `i` has on the adoption of technology by another node `j` that it is connected to depends directly on how 'popular' the node `i` is - which is indicated by its degree.
* We thus imagine a _directed graph_ where each edge points in the direction of the higher degree node to the lower degree node.
* The weight of each such directed edge is proportional to the difference in degrees between these edges, normalized by the *maximum* such difference over all edges in the graph.

# Our experiments
With both the algorithms, we wish to answer the following general question - `What are important rules of thumb in which to run a sharing campaign on facebook, if our goal is to convert as many people as possible in a certain cluster/demographic group`. In particular, we want to answer the following questions. (Our assumption is that, in the social network, there is a certain 'friends circle' or cluster of people sharing similar characteristics whom we would like to _convert_ to adopt our product/technology. We call this the `target nodes`).
* How many 'seed nodes' are required to convert the `target nodes`?
* How many 'seed nodes' are required from the target group itself to convert all the people in the target group?

# Results
TODO

# Acknowledgements
We have used the algorithm implementations (modified by us) by the following people:
* [hhchen1105](https://github.com/hhchen1105/networkx_addon/blob/master/information_propagation/independent_cascade.py)
* [emanuelepesce](https://github.com/emanuelepesce/NetworksSimulator/blob/master/source/Epidemics.py)

The following peoples' work was referenced, but not used:
* [piyushgade](https://github.com/piyushagade/InteractiveViralMarketing/tree/master)
