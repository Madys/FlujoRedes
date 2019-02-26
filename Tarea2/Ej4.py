import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . DiGraph ()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(4,5)
G.add_edge(2,6)
G.add_edge(7,8)
G.add_edge(4,7)
G.add_edge(3,9)
pos = nx.fruchterman_reingold_layout(G,scale=.55,iterations=30)
nx.draw_networkx_nodes(G, pos, node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, width=4, edge_color='b')

labels = {}
labels[1] = r'Mario'
labels[2] = r'Betty'
labels[3] = r'Arturo'
labels[4] = r'Carlos'
labels[5] = r'Anna'
labels[6] = r'Jane'
labels[7] = r'Emily'
labels[8] = r'Andrew'
labels[9] = r'Linn'

nx.draw_networkx_labels(G, pos, labels, font_size=12)
plot.axis('off')
plot.savefig("fig4.eps")
plot.show()