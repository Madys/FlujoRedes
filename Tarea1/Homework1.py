import networkx as nx
import matplotlib.pyplot as plot

# No Dirigido Cíclico = H
H=nx.Graph()
#H.add_nodes_from(xrange(1,8))
H.add_edges_from([(1,2), (2,3), (3,4),(4,5), (1,5), (5,6), (6,7), (7,8), (8,5)])
nx.draw(H)
plot.savefig("fig1.png")
plot.show()












