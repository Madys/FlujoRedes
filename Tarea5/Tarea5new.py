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
from networkx.algorithms.flow import dinitz
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms.flow import boykov_kolmogorov

def PrintGraph(G):
    pos = nx.kamada_kawai_layout(G)
#    pos = nx.fruchterman_reingold_layout(G)
#    pos = nx.spring_layout(G)
     
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
#    edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)
  
def RandNodes(maxi): 
    li=[]
    for i in range(5):
        a=rdm.randint(1,maxi) 
        b=rdm.randint(1,maxi)  
        while a==b:
            b=rdm.randint(1,maxi)
        li.append( [a,b])
    return li

def AddEdges(S):
    scale = 2
    rang = 10
    size = S.number_of_edges()  
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)
    G=nx.Graph(S)
    count=0;
    for j in range(len(S)):
        G.add_node(j)
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count]+rang+1)
        count+=1
    return G
    
def Edmond(G,a,b):
    start_time=time()          
    R = edmonds_karp(G, a, b)
    time_elapsed = time() - start_time  
    return time_elapsed

G=AddEdges(nx.dense_gnm_random_graph(25,50))  
PrintGraph(G)            


    