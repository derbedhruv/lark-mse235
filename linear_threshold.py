#----------------------------------------------------------------------
# DirectedEpidemics
#
# Contains the class which implements methods which simulates epidemics/diffusion
# spreading
# 
# MODIFIED BY: Raunak Rewari, Dhruv Joshi
# 
# ORIGINAL Author: Emanuele Pesce
# SOURCE : https://github.com/emanuelepesce/NetworksSimulator/blob/master/source/Epidemics.py
#----------------------------------------------------------------------
import numpy as np
import random
import networkx as nx
random.seed(88)
    
def linear_threshold(g, seeds, threshold={}):
    """
    g : graph
    seeds : a list of seed nodes

    returns a list of lists of activated nodes by step
    """            
    ''' Inizialization ''' 
    def _infected_neighbour_fraction(n, infected):
        # returns the fraction of neighbours of node 'n' which are infected
        neighbours = g.neighbors(n)
        if len(neighbours) > 0:
            return sum([1 for nv in neighbours if nv in infected])/float(len(neighbours))
        return 0

    # set threshold
    if threshold == {}:
        for n in g.nodes():
            threshold[n] = np.random.uniform()
    
    # add seeds in infected
    infected = set([s for s in seeds])
    activated = [list(infected)]
           
    ''' Epidemics spreading '''
    toSpread = True
    while toSpread == True:
        ''' round of spreading''' 
        toInfect = set()
        for n in g.nodes():
            if n not in infected:
                f = _infected_neighbour_fraction(n, infected)
                # add n to toInfect eventually
                if f > threshold[n]:
                    toInfect.add(n)

        ''' check convergence  '''
        if len(toInfect) > 0: # add infected node to infected set
            infected = infected.union(toInfect)
            activated.append(list(toInfect))

        else: # there no more nodes to infect
            toSpread = False
        
    #return 
    return activated
