import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
B = nx.Graph()
B.add_nodes_from(['$x_1$','$x_2$','$x_3$'], s='o', c='#AA5555', bipartite=0) # Add the node attribute 'bipartite'
B.add_nodes_from(['$f_a$','$f_b$','$f_c$','$f_d$'], s='s', c='#55AAAA', bipartite=1)
B.add_edges_from([('$x_1$','$f_a$'),('$x_1$','$f_b$'),('$x_2$','$f_a$'),('$x_2$','$f_b$'),('$x_2$','$f_c$'),('$x_3$','$f_c$'),('$x_3$','$f_d$')])

pos = dict()
X, Y = bipartite.sets(B)
pos.update((n, (i, 1)) for i, n in enumerate(X))
pos.update((n, (i+0.5, 2)) for i, n in enumerate(Y))

disjointSetCount = 2
for disjointSet in range(0, disjointSetCount):
    nx.draw(
        B,
        pos,
        with_labels=True,
        font_size=14,
        node_shape='s' if disjointSet == 1 else 'o',
        node_color='#FFEEEE' if disjointSet == 1 else '#EEEEFF',
        node_size=1000,
        nodelist=[
            sNode[0] for sNode in filter(lambda x: x[1]["bipartite"]== disjointSet, B.nodes(data=True))
        ]
    )

plt.savefig("15_Graphical_Models_12b.png")
plt.show()