"""

"""
__author__ = """Aned Esquerra Arguelles (anedesquerra@gmail.com)"""

try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx

# User defined functions
def generate_img_filename(base_name, ext_name):
    current_datetime = dt.datetime.now()
    key = base_name + str(current_datetime.year) + \
          str(current_datetime.month) + \
          str(current_datetime.day) + \
          str(current_datetime.hour) + \
          str(current_datetime.minute) + \
          str(current_datetime.second) + \
          "." + ext_name
    return key


# main code
# creating graph by adding vertices and edges

G = nx.DiGraph()
G.add_edge(1, 2, length=5, weight=0.1)

positions = nx.spring_layout(G)

# Drawing resulting graph
nx.draw_networkx_nodes(G, positions, node_color='b', node_size=500)
nx.draw_networkx_edges(G, positions, style='dashed', edge_color='red', alpha=0.5)
nx.draw_networkx_edge_labels(G, positions)
nx.draw_networkx_labels(G, positions, font_size=9,
                        font_color='white', font_family='sans-serif')

plt.axis('off')
plt.savefig("../images/NF_H1_graph_sect03.eps")
plt.show()
