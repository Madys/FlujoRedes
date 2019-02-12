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
pos = {1:(300, 400), 2:(100,300), 3:(250, 300), 4:(350,300), 5:(450,200), 6:(150,200),7:(300,200),8:(250,100)}

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(4,5)
G.add_edge(2,6)
G.add_edge(7,8)
G.add_edge(4,7)

nx.draw_networkx_nodes(G, pos, node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.8, edge_color='black')

labels = {}
labels[1] = r'Mario'
labels[2] = r'Betty'
labels[3] = r'Arturo'
labels[4] = r'Carlos'
labels[5] = r'Anna'
labels[6] = r'Jane'
labels[7] = r'Emily'
labels[8] = r'Andrew'

nx.draw_networkx_labels(G, pos, labels, font_size=12)
plot.xlim(50,500)
plot.axis('off')
plot.savefig("4.eps")
plot.show()