# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:38:55 2019

@author: Madys
"""
import networkx as nx
import numpy as np 
import pandas as pd
import random as rdm
import matplotlib.pyplot as plt
from time import time
from scipy.stats import truncnorm
from networkx.algorithms.flow import dinitz
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms.flow import boykov_kolmogorov

def ReadGraph(adress):
    ds = pd.read_csv(adress, header=None)
    G = nx.from_pandas_adjacency(ds)
    return G
def PrintGraph(G,widths):
#    pos=nx.fruchterman_reingold_layout(G)
    widths[:] = [x/10*x/10 for x in widths]
    pos=nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='g', node_shape='o')
    print(widths)   
    nx.draw_networkx_edges(G, pos, edge_color='black', width=widths)   
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=12 )
    plt.axis('off')
    
G=ReadGraph("Grafo1.csv")
df = pd.read_csv('Grafo1_edges.csv', index_col=None)
W = list(df["edges"])
PrintGraph(G,W)








