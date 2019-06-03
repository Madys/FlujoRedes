# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:15:32 2019
@author: Madys
"""
import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . MultiGraph ()

G.add_edge(1,2, weight=1)
G.add_edge(1,2, weight=3)
G.add_edge(2,3, weight=3)
G.add_edge(1,3, weight=3)
G.add_edge(4,5, weight=1)
G.add_edge(4,5, weight=3)

blue=[(1,2),(4,5)]
red=[(1,2),(2,3),(1,3),(4,5)]

pos = {1:(200, 100), 2:(100,400), 3:(200, 700), 4:(500,700), 5:(650,400)}

nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='r', node_shape='o',alpha=0.6)
nx.draw_networkx_edges(G, pos, edgelist=blue,width=6, alpha=0.5,
edge_color='b', style='dashed')

nx.draw_networkx_edges(G, pos, edgelist=red,width=4, alpha=0.5,
edge_color='r')
labels = {}
labels[1] = r'Automatica'
labels[2] = r'Electrica'
labels[3] = r'Fisica'
labels[4] = r'Informatica'
labels[5] = r'Cibernetica'

nx.draw_networkx_labels(G, pos, labels, font_size=13)

plot.xlim(20,800)
plot.axis('off')
plot.savefig("9.eps")
plot.show()