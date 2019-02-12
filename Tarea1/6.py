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


pos = {1:(200, 350), 2:(550,350), 3:(650, 220), 4:(400,100), 5:(150,220)}

nx.draw_networkx_nodes(G, pos, nodelist=node1,node_size=400, node_color='r', node_shape='o')
nx.draw_networkx_nodes(G, pos, nodelist=node2,node_size=400, node_color='y', node_shape='o')
nx.draw_networkx_edges(G, pos,width=1, alpha=0.8, edge_color='black')

labels = {}
labels[1] = r'Mayra'
labels[2] = r'Andrew'
labels[3] = r'Emily'
labels[4] = r'Laura'
labels[5] = r'Oliver'



nx.draw_networkx_labels(G, pos, labels, font_size=12)
plot.xlim(20,1000)
plot.axis('off')
plot.savefig("6.eps")

plot.show()