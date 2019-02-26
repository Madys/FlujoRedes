import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . DiGraph ()

G.add_edge(1,2,calle='c')
G.add_edge(2,3,calle='c')
G.add_edge(5,4,calle='b')
G.add_edge(6,5,calle='b')
G.add_edge(8,9,calle='a')
G.add_edge(7,8,calle='a')
G.add_edge(1,4,calle='19')
G.add_edge(4,7,calle='19')
G.add_edge(8,5,calle='21')
G.add_edge(5,2,calle ='21')
G.add_edge(3,6,calle ='23')
G.add_edge(6,9,calle ='23')

pos = nx.spectral_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)


plot.axis('off')
plot.savefig("fig5.eps")
plot.show()