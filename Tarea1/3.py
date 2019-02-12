# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:37:20 2019
@author: Madys
"""

import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . Graph ()

G.add_edge(1,2)
G.add_edge(3,4)
G.add_node(5)
G.add_node(6)
apareados={1,2,3,4,5}
noApareado={6}
pos = {1:(200, 350), 2:(550,350), 3:(650, 220), 4:(400,100), 5:(150,220),6:(100,100)}

nx.draw_networkx_nodes(G, pos,nodelist=apareados,node_size=400, node_color='r', node_shape='o')
nx.draw_networkx_nodes(G, pos,nodelist=noApareado, node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos,width=1, alpha=0.8, edge_color='black')

labels = {}
labels[1] = r'Boxer'
labels[2] = r'Bulldog'
labels[3] = r'Rottweiler'
labels[4] = r'Stanford'
labels[5] = r'Poodle'
labels[6] = r'Beagle'

nx.draw_networkx_labels(G, pos, labels, font_size=12)
plot.xlim(20,730)
plot.axis('off')
plot.savefig("3.eps")
plot.show()