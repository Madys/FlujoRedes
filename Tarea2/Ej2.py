
import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . Graph ()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(4,5)
G.add_edge(2,6)
G.add_edge(3,8)
G.add_edge(7,8)
G.add_edge(4,8)
G.add_edge(4,7)
pos=nx.fruchterman_reingold_layout(G,scale=.45)

nx.draw_networkx_nodes(G, pos, node_size=1800, node_color='g', node_shape='o')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='red')

labels = {}
labels[1] = r'$ Mario $'
labels[2] = r'$Betty$'
labels[3] = r'$Arturo$'
labels[4] = r'$Carlos$'
labels[5] = r'$Anna$'
labels[6] = r'$Jane$'
labels[7] = r'$Emily$'
labels[8] = r'$Andy$'

nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color='w')

plot.axis('off')
plot.savefig("fig2.eps")

plot.show()