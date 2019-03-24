"""
Created on Tue Mar 12 19:09:10 2019
@author: Madys
"""
import networkx as nx
import numpy as np 
import pandas as pd
import random as rdm
import matplotlib.pyplot as plt
from time import time
from scipy.stats import truncnorm

def PrintImage(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
#    edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)
    
G=nx.balanced_tree(3, 3)
D=nx.barbell_graph(6, 1)
C=nx.complete_graph(6)
A=nx.circular_ladder_graph(8)
T=nx.dorogovtsev_goltsev_mendes_graph(3)
B=nx.lollipop_graph(5, 2, create_using=None)
R=nx.star_graph(10, create_using=None)
S=nx.wheel_graph(8, create_using=None)


def GenerarGrafos():  
    size=16
    for i in range(1,5):       
        for j in range(10):
            df = pd.DataFrame()
            df = nx.to_pandas_adjacency(nx.circular_ladder_graph(size))
            df.to_csv("CL"+str(size)+"_"+str(j)+".csv")
            df = nx.to_pandas_adjacency(nx.star_graph(size))
            df.to_csv("Star"+str(size)+"_"+str(j)+".csv")
            df = nx.to_pandas_adjacency(nx.complete_graph(size))
            df.to_csv("Cmp"+str(size)+"_"+str(j)+".csv")
        size*=2;
        
def PrintGraph(G):
    pos = nx.spectral_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
    edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)

scale = 2
range = 10
size = 63
S = nx.complete_graph(8)
e=S.edges(nbunch=None, data=True, default=None)

#PrintImage(S)
X = truncnorm(a=-range/scale, b=+range/scale, scale=scale).rvs(size=size)
X = X.round().astype(int)
#bins = 2 * range + 1
#plt.hist(X, bins)
G=nx.Graph()
count=0;
for i in e:
    print(i)
    G.add_edge(i[0],i[1],weight=X[count]+10)
    count=count+1

PrintGraph(G)
