# Importing related packages
"""

"""
__author__ = """Aned Esquerra Arguelles (anedesquerra@gmail.com)"""

try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx

# main code
# Creating graph representing the computers' network topology of UNIMETA
# AUSG acronym for Acyclic Undirected Simple Graph
AUSG = nx.Graph()

AUSG.add_edge('DC', 'VIn', weight=1.6)
AUSG.add_edge('DC', 'VAd', weight=1.6)
AUSG.add_edge('DC', 'AsC', weight=1.6)

# Universitary research vice-rectoship computers' distribution
AUSG.add_edge('DC', 'VFi', weight=1.6)
AUSG.add_edge('VFi', 'i01', weight=0.1)
AUSG.add_edge('VFi', 'i02', weight=0.1)
AUSG.add_edge('VFi', 'i03', weight=0.22)
AUSG.add_edge('VFi', 'i04', weight=0.15)
AUSG.add_edge('VFi', 'i05', weight=0.14)

# Universitary well-being computers' distribution
AUSG.add_edge('DC', 'BUn', weight=1.6)
AUSG.add_edge('BUn', 'u01', weight=0.12)
AUSG.add_edge('BUn', 'u02', weight=0.12)

# Universitary Library computers' distribution
AUSG.add_edge('DC', 'Bib', weight=1.6)
AUSG.add_edge('Bib', 'b01', weight=0.1)
AUSG.add_edge('Bib', 'b02', weight=0.1)
AUSG.add_edge('Bib', 'b03', weight=0.1)
AUSG.add_edge('Bib', 'b04', weight=0.1)
AUSG.add_edge('Bib', 'b05', weight=0.1)
AUSG.add_edge('Bib', 'b06', weight=0.1)

# Defining type of cabbling by distance
# (UTP wire < 300m, optical fiber > 300 m)
optical_fiber = [(u, v) for (u, v, d) in
                 AUSG.edges(data=True) if d['weight'] >= 0.3]
UTP_wire = [(u, v) for (u, v, d) in
            AUSG.edges(data=True) if d['weight'] < 0.3]

positions = nx.spring_layout(AUSG)

# Drawing and saving the resulted graph
nx.draw_networkx_nodes(AUSG, positions, node_size=500)
nx.draw_networkx_edges(AUSG, positions, edgelist=optical_fiber, width=2)
nx.draw_networkx_edges(AUSG, positions, edgelist=UTP_wire, width=1,
                       alpha=0.5, edge_color='blue', style='dashed')
nx.draw_networkx_labels(AUSG, positions, font_size=10,
                        font_family='sans-serif')

#plt.title("Syntactic analyzer tree on Mathematics expression")
plt.axis("off")

print("Saving graph image to file...")
plt.savefig("../images/NF_H1_graph_sect01.eps", bbox_inches='tight')
plt.show()
