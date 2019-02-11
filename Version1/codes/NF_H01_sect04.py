"""
 Creating graph representing abstractly an tree structure
 of a syntactic analyzer of a compiler for
 mathematical expression

 Hints
 CDSG acronym for Cyclic Undirected Simple Graph

"""
__author__ = """Aned Esquerra Arguelles (anedesquerra@gmail.com)"""

try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx

# Creating the specific graph using dictionaries
positions = {"*": (0, 0), "+": (-500, -100), "-": (500, -100),
             "tmp": (-750, -200), "x": (-250, -200), "pos": (250, -200),
             "^": (750, -200), "t": (500, -300), "2": (1000, -300)
             }
links = {("*", "+"), ("*", "-"), ("+", "tmp"),
         ("+", "x"), ("-", "pos"), ("-", "^"),
         ("^", "t"), ("^", "2")}

CDSG = nx.DiGraph()
CDSG.add_nodes_from(positions)
CDSG.add_edges_from(links)

# Drawing all graph components
nx.draw_networkx_edges(CDSG, positions, edges=links, width=1, edge_color="black",
                       style="solid")
nx.draw_networkx_nodes(CDSG,
                       positions,
                       node_color="#066d8b",
                       node_shape="o",
                       node_size=900,
                       alpha=0.5
                       )

nx.draw_networkx_labels(CDSG, positions, font_size=11, font_color="blue",
                        font_family="sans-serif")

plt.title("Tree on mathematical expression (tmp+x)*(pos - t^2)")
plt.axis("off")

print("Saving graph image to file...")
plt.savefig("../images/NF_H1_graph_sect04.eps", bbox_inches="tight")
plt.show()
