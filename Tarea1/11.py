# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:00:30 2019
@author: Madys
"""

import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . MultiDiGraph ()

G.add_edge(1,2, weight=3)
G.add_edge(1,2, weight=5)
G.add_edge(1,2, weight=6)
G.add_edge(2,3, weight=3)
G.add_edge(2,3, weight=5)
G.add_edge(2,3, weight=6)
G.add_edge(3,4, weight=3)
G.add_edge(4,5, weight=3)
G.add_edge(4,5, weight=5)
G.add_edge(5,6, weight=3)
G.add_edge(6,7, weight=6)
G.add_edge(7,1, weight=6)

blue=[(1,2),(2,3),(3,4),(4,5),(5,6)]
red=[(1,2),(2,3),(4,5)]
green=[(1,2),(2,3),(6,7),(7,1)]

pos = {1:(400, 700), 2:(700,600), 3:(550, 400), 4:(400,200), 5:(300,100),6:(150,200), 7:(100
       ,400)}

nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, edgelist=blue,width=6, alpha=0.5,
edge_color='b', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=green,width=5, alpha=0.5,
edge_color='g')
nx.draw_networkx_edges(G, pos, edgelist=red,width=4, alpha=0.5,
edge_color='r')

labels = {}
labels[1] = r'Casa'
labels[2] = r'A'
labels[3] = r'B'
labels[4] = r'C'
labels[5] = r'D'
labels[6] = r'E'
labels[7] = r'F'

nx.draw_networkx_labels(G, pos, labels, font_size=12)
plot.xlim(20,800)
plot.axis('off')
plot.savefig("11.eps")
plot.show()