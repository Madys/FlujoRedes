import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . DiGraph ()


G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(3,5)
G.add_edge(1,6)

G.add_edge(2,6)



pos = {1:(50, 350), 2:(250,350), 3:(450, 350), 4:(600,350), 5:(550,340), 6:(450,330)}
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.8, edge_color='black')

labels = {}
labels[1] = r'$v1$'
labels[2] = r'$v2$'
labels[3] = r'$v3$'
labels[4] = r'$e21$'
labels[5] = r'$e14$'
labels[6] = r'$v6$'


nx.draw_networkx_labels(G, pos, labels, font_size=12)
plot.xlim(20,800)
plot.axis('off')
plot.savefig("12.eps")

plot.show()