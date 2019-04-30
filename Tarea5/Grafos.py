import networkx as nx
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

def GenerateGraph(nodes,edges,address):
    S=nx.dense_gnm_random_graph(nodes,edges)
    scale = 2
    rang = 10
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=edges)
    X = X.round().astype(int)+rang+2
    G=nx.Graph()
    count=0;
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count])
        count+=1
    df = pd.DataFrame()
    df = nx.to_pandas_adjacency(G, dtype=int, weight='capacity')
    df.to_csv(address, index=None, header=None)
    
def Print(graph,address, pos_address,fig):
    ds = pd.read_csv(graph, header=None)
    G = nx.from_pandas_adjacency(ds)
    pos=nx.fruchterman_reingold_layout(G)
    X=[]
    for edge in G.edges():    
        X.append( G.edges[edge]['weight'] )  
    X[:] = [x/10*x/8 for x in X]  
    labels = {}
    for i in G.nodes:     
        labels[i]=str(i)         
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='y', node_shape='o')   
    nx.draw_networkx_edges(G, pos, edge_color='black', width=X)     
    nx.draw_networkx_labels(G, pos, labels, font_size=8 )
    plt.axis('off')
    plt.savefig(fig,dpi=500)
    df = pd.DataFrame(pos)
    df.to_csv(address, index=None, header=None)
    return(G)


