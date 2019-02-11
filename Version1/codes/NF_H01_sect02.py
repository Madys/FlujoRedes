"""

"""
__author__ = """Aned Esquerra Arguelles (anedesquerra@gmail.com)"""

try:
    import matplotlib.pyplot as plt
except:
    raise
import networkx as nx

#User defined functions
def generate_filename(base_name, ext_name):
	currentDT = dt.datetime.now()
	key = str(currentDT.year) + \
		str(currentDT.month) + \
		str(currentDT.day) + \
		str(currentDT.hour) + \
		str(currentDT.minute) + \
		str(currentDT.second)
	return base_name + key + '.' + ext_name

#main code
#creating graph by adding vertices and edges

G = nx.Graph()
G.add_edges_from((
	[(1, 2), (1, 10), (1, 13),
	 (2, 3), (2,11),
	 (3, 4), (3, 6), (3, 11), (3, 12), (3, 13),
	 (4, 5), (4, 12),(4, 13),
	 (5, 9), (5, 10),
	 (6, 7), (6, 13),
	 (7, 8),
	 (8, 9), (8, 10), (8, 12), (8, 13),
	 (9, 10),
	 (10, 11)]
	))



#Drawing and saving the resulted graph
nx.draw(G)
plt.savefig("../images/NF_H1_graph_sect02.eps")
plt.show()