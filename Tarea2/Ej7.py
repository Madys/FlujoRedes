import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . MultiGraph ()


G.add_edge(1,2, weight=1)
G.add_edge(2,3 ,weight=1)
G.add_edge(3,4, weight=1)
G.add_edge(4,5, weight=1)
G.add_edge(5,6, weight=1)
G.add_edge(5,6,weight=2)
G.add_edge(6,7, weight=1)
black=[(1,2),(2,3),(3,4),(4,5),(6,7)]
blue=[(5,6)]
red=[(5,6)]
pos = nx.kamada_kawai_layout(G, scale=.2)

nx.draw_networkx_nodes(G, pos ,node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos,edgelist=black,width=1,edge_color='black', alpha=0.8)
nx.draw_networkx_edges(G, pos, edgelist=blue,width=6, alpha=0.5,
edge_color='b', style='dashed')
nx.draw_networkx_edges(G, pos, edgelist=red,width=4, alpha=0.5,
edge_color='r')
labels = {}
labels[1] = r'Santiago'
labels[2] = r'1'
labels[3] = r'2'
labels[4] = r'3'
labels[5] = r'Caballeria'
labels[6] = r'Caballeria'
labels[7] = r'Holguin'

nx.draw_networkx_labels(G, pos, labels, font_size=12)

plot.axis('off')
plot.savefig("fig7.eps")
plot.show()