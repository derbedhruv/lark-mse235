# Stanford MS&E 235 Spring 2017 Course Project
The project primarily looks at the problem of running an effective facebook campaign to target a specific demographic.

In particular, we model how a viral campaign would spread if a varying number of seed nodes was used and a specific demographic of users was targeted on facebook. We make use of the (facebook ego network)[https://snap.stanford.edu/data/egonets-Facebook.html]. We also use the following two algorithms to model the diffusion of _adoption of a particular product_ through virally shared content that encourages a user (node) to adopt the particular technology:
* Linear Thresholding
* Independent Cascade

# Acknowledgements
We have used the algorithm implementations (modified by us) by the following people:
* (hhchen1105)[https://github.com/hhchen1105/networkx_addon/blob/master/information_propagation/independent_cascade.py]
* (emanuelepesce)[https://github.com/emanuelepesce/NetworksSimulator/blob/master/source/Epidemics.py]

The following peoples' work was referenced, but not used:
* (piyushgade)[https://github.com/piyushagade/InteractiveViralMarketing/tree/master]
