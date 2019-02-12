# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:44:18 2019
@author: Madys
"""

import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . MultiDiGraph ()

G.add_edge(1,2, weight=3)
G.add_edge(1,2, weight=5)
G.add_edge(1,2, weight=6)
G.add_edge(2,3, weight=4)
G.add_edge(2,5, weight=3)
G.add_edge(2,5, weight=5)
G.add_edge(1,4, weight=4)
G.add_edge(1,4, weight=3)
G.add_edge(4,5, weight=5)
G.add_edge(4,5, weight=3)
G.add_edge(1,6, weight=3)
G.add_edge(1,6,weight=2)
G.add_edge(6,7, weight=1)
G.add_edge(6,7, weight=4)
G.add_edge(1,8, weight=5)
G.add_edge(1,8, weight=4)
G.add_edge(1,8, weight=2)
G.add_edge(8,9, weight=5)
G.add_edge(8,9, weight=4)

blue=[(1,2),(2,3),(2,5),(1,4),(4,5),(1,6),(6,7),(1,8),(8,9)]
red=[(1,2),(2,5),(1,4),(4,5),(1,6),(6,7),(1,8),(8,9)]
green=[(1,2),(2,5),(1,8)]

pos = {1:(400, 700), 2:(300,300), 3:(150, 100), 4:(400,200), 5:(300,100),6:(250,500), 7:(100
       ,100), 8:(500, 300), 9:(700,100)}

nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, edgelist=blue,width=6, alpha=0.5,
edge_color='b', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=green,width=5, alpha=0.5,
edge_color='g')
nx.draw_networkx_edges(G, pos, edgelist=red,width=4, alpha=0.5,
edge_color='r')
labels = {}
labels[1] = r'Nacimiento'

nx.draw_networkx_labels(G, pos, labels, font_size=12)

plot.xlim(20,800)
plot.axis('off')
plot.savefig("10.eps")
plot.show()