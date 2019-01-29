from networkx import nx
import matplotlib.pyplot as plt # otro
G = nx.Graph()
G.add_edge(1, 2)
nx.draw(G)
plt.savefig("prueba.png")
plt.savefig("prueba.eps")
