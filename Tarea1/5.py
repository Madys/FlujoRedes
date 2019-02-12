# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:26:08 2019

@author: Madys
"""
import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . DiGraph ()

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(6,5)
G.add_edge(4,5)
G.add_edge(8,9)
G.add_edge(7,8)
G.add_edge(1,4)
G.add_edge(4,7)
G.add_edge(8,5)
G.add_edge(5,2)
G.add_edge(3,6)
G.add_edge(6,9)


pos = {1:(50, 350), 2:(250,350), 3:(450, 350), 4:(50,200), 5:(250,200), 6:(450,200),7:(50,50),8:(250,50),9:(450,50)}
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.8, edge_color='black')



plot.xlim(0,500)
plot.axis('off')
plot.savefig("5.eps")

plot.show()