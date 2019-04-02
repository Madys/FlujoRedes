# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 01:37:48 2019

@author: Madys
"""

G=AddEdges(nx.circular_ladder_graph(10))
def PrintGraph(G):
    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
#    edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)
    
PrintGraph(G)
    
    