import matplotlib.pyplot as plot
import networkx as nx

G  =  nx . Graph ()
G.add_edge('Sendero','Santiago Tapia')
G.add_edge('Santiago Tapia','San Nicolas')
G.add_edge('San Nicolas','Anahuac')
G.add_edge('Anahuac','Universidad')
G.add_edge('Universidad','Ninos Heroes')
G.add_edge('Ninos Heroes','Regina')
G.add_edge('Regina','General Anaya')

positions = nx.spring_layout(G, scale=.15)

nx.draw_networkx_nodes(G, positions, node_size=500, node_color='y')
nx.draw_networkx_edges(G, positions, width=1,alpha=1, edge_color='b')
nx.draw_networkx_labels(G, positions, font_size=12,font_family='sans-serif')
plot.axis('off')
plot.savefig("fig1.eps")
plot.show()