# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:15:32 2019
@author: Madys
"""

import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . Graph ()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
pos = {1:(200, 50), 2:(250,100), 3:(300, 150), 4:(350,200), 5:(400,250), 6:(450,300),7:(500,350),8:(550,400)}

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(6,7)
G.add_edge(7,8)

nx.draw_networkx_nodes(G, pos, node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.8, edge_color='black')

labels = {}
labels[1] = r'Sendero'
labels[2] = r'Santiago Tapia'
labels[3] = r'San Nicolas'
labels[4] = r'Anahuac'
labels[5] = r'Universidad'
labels[6] = r'Ninos Heroes'
labels[7] = r'Regina'
labels[8] = r'General Anaya'

nx.draw_networkx_labels(G, pos, labels, font_size=8)
plot.xlim(0,600)
plot.axis('off')
plot.savefig("1.eps")
plot.show()