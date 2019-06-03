# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:44:07 2019

@author: Madys
"""
import networkx as nx
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from time import time
from scipy.stats import truncnorm
from networkx.algorithms.flow import edmonds_karp

def ReadGraph(graph,position):
    ds = pd.read_csv(graph, header=None)
    G = nx.from_pandas_adjacency(ds)
    pos=pd.read_csv(position,header=None)
    return G,pos

def PrintImage(G,pos):
    labels = {}
    for u, v, data in G.edges(data=True):
        labels[(u, v)] = data['flow']
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
    edge_labels=nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=7,label_pos=.5)
  
def Edmond(G,a,b):
    start_time=time()         
    R = edmonds_karp(G, a, b,capacity="weight")
    for i in range(20):
        print(1)
    time_elapsed = time() - start_time  
    return time_elapsed

def PrintRes(G,pos,bests, aceptables,malos,name): 
    negros=[]
    flowrojos=[]
    rojos=[]
    negrospesos=[]
    rojospesos=[]
    maxi=0
    labels = {}
    for edge in G.edges():            
        if G.edges[edge]['flow']==0:            
           negros.append(edge)  
           negrospesos.append( G.edges[edge]['capacity'] )
        elif G.edges[edge]['flow']>0:                                                                                                                         
           rojos.append(edge) 
           rojospesos.append( G.edges[edge]['capacity'] ) 
           flowrojos.append(G.edges[edge]['flow'] )         
    for u, v, data in G.edges(data=True):
       if data['flow']>0:
           labels[(u, v)] = data['flow']
    flowrojos[:] = [x+10 for x in flowrojos] 
    maxi=max(flowrojos)      
    negrospesos[:] = [x/10*x/7 for x in negrospesos] 
    rojospesos[:] = [x/10*x/7 for x in rojospesos] 
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='y', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=bests, node_size=300, node_color='r', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=aceptables, node_size=250, node_color='b', node_shape='o')   
    nx.draw_networkx_nodes(G, pos,nodelist=malos, node_size=200, node_color='#a0a382', node_shape='o')   
    nx.draw_networkx_edges(G, pos, edgelist=negros, edge_color='black', width= negrospesos,arrows=False)   
    nx.draw_networkx_edges(G, pos,edgelist=rojos, edge_cmap=plt.cm.PuRd, width=rojospesos,edge_color=flowrojos,edge_vmin=0,arrows=False,edge_vmax=maxi) 
    nx.draw_networkx_edge_labels(G,pos,edgelist=rojos,edge_labels=labels,font_size=7,label_pos=.5)
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw_networkx_labels(G, pos, labels, font_size=9 )
    plt.axis('off')       
    plt.savefig(name,dpi=500)
            
def AddEdges(S):
    scale = 2
    rang = 10
    size = S.number_of_edges()  
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)+rang+2
    G=nx.Graph()
    count=0;
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count])
        count+=1        
    return G,X
    df = pd.DataFrame()
    df = nx.to_pandas_adjacency(G, dtype=int, weight='capacity')
    df.to_csv("grafo1.csv")
    edgs={"edges":X}
    df=pd.DataFrame(edgs)
    df.to_csv("grafo1_edges.csv", index=None)

def AddEdges1(S):
    scale = 2
    rang = 10
    size = S.number_of_edges()  
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)+rang+2
    G=nx.Graph()
    count=0;
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count])
        count+=1
    df = pd.DataFrame()
    df = nx.to_pandas_adjacency(G, dtype=int, weight='capacity')
    df.to_csv("grafo1.csv")
    edgs={"edges":X}
    df=pd.DataFrame(edgs)
    df.to_csv("grafo1_edges.csv", index=None)

def Atributes(G,name):   
    dic={}  
    Nodes=G.nodes;
    dic["Nodo"]=Nodes
    dic["Grado"]=[G.degree(i) for i in Nodes]
    dic["CoefA"]=[nx.clustering(G,i) for i in Nodes]
    dic["CentCe"]=[nx.closeness_centrality(G,i) for i in Nodes]
    dic["CentCa"]=[nx.load_centrality(G,i) for i in Nodes]
    dic["Excent"]=[nx.eccentricity(G,i) for i in Nodes]
    PageR=nx.pagerank(G,weight="capacity")
    dic["PageR"]=[PageR[i] for i in Nodes]
    df=pd.DataFrame(dic)
    df.to_csv(name, index=None)     
  
def Time(G,name):
    dic={"Fuente":[], "Sumidero":[] , "Media":[], "Mediana":[], "Std":[], "MaxFlow":[]}  
    Nodes=G.nodes;
    for i in Nodes:
        for j in Nodes:          
            if i!=j: 
                t=[]                    
                for k in range(10):
                   t.append(Edmond(G,i,j))                              
                dic["Fuente"].append(i)    
                dic["Sumidero"] .append(j)  
                dic["Media"].append(np.mean(t))    
                dic["Mediana"].append(np.median(t))    
                dic["Std"].append(np.std(t))
                dic["MaxFlow"].append(nx.maximum_flow_value(G,i,j,capacity="weight"))
    df=pd.DataFrame(dic)
    df.to_csv(name, index=None)    
 
    
def Histogramas():
    cont=0
    nombres=["Distribución de grado ","Coeficiente de agrupamiento ", "Centralidad de cercanía ", "Centralidad de carga ", "Excentricidad " , "Rango de página "]
    matrix=["matrix1.csv","matrix2.csv","matrix3.csv","matrix4.csv","matrix5.csv"]
    caract=["Grado","CoefA","CentCe","CentCa", "Excent","PageR"] 
    for i in matrix:
        H= pd.read_csv(i)
        car=0
        for j in caract: 
            fig = plt.figure(figsize=(5, 5))
            ax = fig.add_subplot(1, 1, 1)
            his = ax.hist(H[j],bins=len(H[caract]), facecolor='#8a36f8', alpha=0.75)
            ax.set_xlabel(nombres[car] + "grafo "+str(cont))
            ax.set_ylabel("Ocurencia")
    #        plt.savefig("histograma"+ y + j + ".png", bbox_inches="tight", dpi=100)
            plt.savefig(j+"_grafo_"+str(cont) + ".eps", bbox_inches="tight", dpi=100)     
            plt.show() 
            car+=1
        cont+=1
        
def Todo(G,name):
    dic={"Fuente":[],
         "Sumidero":[] , 
         "Media":[],
         "Mediana":[],
         "Std":[],
         "Flujomaximo":[],
         "DistG":[],
         "CoefA":[],
         "CentCe":[],
         "CentCa":[],
         "Excent":[],
         "PageR":[]}    
    Nodes=G.nodes;
    for i in Nodes:
        for j in Nodes:          
            if i!=j: 
                t=[]                    
                for k in range(10):
                   t.append(Edmond(G,i,j))                 
                dic["Fuente"].append(i)    
                dic["Sumidero"] .append(j)  
                dic["Media"].append(np.mean(t))    
                dic["Mediana"].append(np.median(t))    
                dic["Std"].append(np.std(t))
                dic["Flujomaximo"].append(nx.maximum_flow_value(G,i,j,capacity="weight"))               
                dic["DistG"].append(G.degree(i))
                dic["CoefA"].append(nx.clustering(G,i))
                dic["CentCe"].append(nx.closeness_centrality(G,i))
                dic["CentCa"].append(nx.load_centrality(G,i))
                dic["Excent"].append(nx.eccentricity(G,i))
                PageR=nx.pagerank(G,weight="capacity")
                dic["PageR"].append(PageR[i])  
    df=pd.DataFrame(dic)
    df.to_csv(name, index=None)
