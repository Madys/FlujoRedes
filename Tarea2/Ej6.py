
import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . DiGraph ()

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,5)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(4,5)
node1 = {1,2}
node2 = {3,4,5}

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=node1,node_size=100, node_color='r', node_shape='o',alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=node2,node_size=100, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos,width=5, alpha=0.4, edge_color='b')

labels = {}
labels[1] = r'Mayra'
labels[2] = r'Andrew'
labels[3] = r'Emily'
labels[4] = r'Laura'
labels[5] = r'Oliver'

pos1=pos
for i in pos:    
    pos1[i][1] = pos1[i][1] -0.15    
nx.draw_networkx_labels(G, pos1, labels, font_size=14)

plot.axis('off')
plot.savefig("fig6.eps")
plot.show()