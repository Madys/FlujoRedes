import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . Graph ()

G.add_edge(1,2)
G.add_edge(3,4)
G.add_node(5)
G.add_node(6)
apareados={1,2,3,4,5}
noApareado={6}
pos = nx.kamada_kawai_layout(G,scale=.45)

nx.draw_networkx_nodes(G, pos,nodelist=apareados,node_size=4400, node_color='r', node_shape='o')
nx.draw_networkx_nodes(G, pos,nodelist=noApareado, node_size=2800, node_color='y', node_shape='s')
nx.draw_networkx_edges(G, pos,width=6, alpha=0.6, edge_color='b')

labels = {}
labels[1] = r'Boxer'
labels[2] = r'Bulldog'
labels[3] = r'Rottweiler'
labels[4] = r'Stanford'
labels[5] = r'Poodle'
labels[6] = r'Beagle'

nx.draw_networkx_labels(G, pos, labels, font_size=12,font_color='w')

plot.axis('off')
plot.savefig("fig3.eps")
plot.show()

