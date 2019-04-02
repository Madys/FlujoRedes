"""
Created on Tue Mar 12 19:09:10 2019
@author: Madys
"""
import networkx as nx
import numpy as np 
import pandas as pd
import random as rdm
import matplotlib.pyplot as plt
from time import time
from scipy.stats import truncnorm
from networkx.algorithms.flow import dinitz
from networkx.algorithms.flow import edmonds_karp
from networkx.algorithms.flow import boykov_kolmogorov

def PrintGraph(G):
    pos = nx.spectral_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
    edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)
  
def RandNodes(maxi): 
    li=[]
    for i in range(5):
        a=rdm.randint(1,maxi) 
        b=rdm.randint(1,maxi)  
        while a==b:
            b=rdm.randint(1,maxi)
        li.append( [a,b])
    return li

def AddEdges(S):
    scale = 2
    rang = 10
    size = S.number_of_edges()  
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)
    G=nx.Graph(S)
    count=0;
    for j in range(len(S)):
        G.add_node(j)
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count]+rang+1)
        count+=1
    return G
    
def Edmond(G,a,b):
    start_time=time()          
    R = edmonds_karp(G, a, b)
    time_elapsed = time() - start_time  
    return time_elapsed

def Din(G,a,b):   
    start_time=time()           
    R = dinitz(G, a, b)
    time_elapsed = time() - start_time  
    return time_elapsed

def Boyk(G,a,b):
    start_time=time()          
    R = boykov_kolmogorov(G, a, b)
    time_elapsed = time() - start_time  
    return time_elapsed

def GenerateDic():   
    dic={}  
    for j in ["Generador","Algoritmo","Nodos","Edges", "Fs","Mediana","Media","Desv","Var","Densidad"]:                 
        dic[j]=[]      
    return dic
  
def Asign(dic, gen,alg,nod, edg, fs, median,aver,desv,var,dens):
    dic["Generador"].append(gen)
    dic["Algoritmo"].append(alg)
    dic["Nodos"].append(nod)
    dic["Fs"].append(fs)
    dic["Edges"].append(edg)
    dic["Mediana"].append(median)
    dic["Media"].append(aver)
    dic["Desv"].append(desv)
    dic["Var"].append(var)
    dic["Densidad"].append(dens)
               
def GenerateGraphs(size, base):
    dic=GenerateDic()
    for i in range(1,5):  
        for j in range(10):              
            G=AddEdges(nx.dense_gnm_random_graph(size,int(size*size*0.03 ))) 
            nodes=RandNodes(size-1)          
            for k in range (5):               
                edmond=[]
                din=[]
                boyk=[]
                for l in range(5):
                    edmond.append(Edmond(G,nodes[l][0],nodes[l][1]))
                    din.append(Din(G,nodes[l][0],nodes[l][1]))
                    boyk.append(Boyk(G,nodes[l][0],nodes[l][1]))
                Asign(dic, "dense","Edmond", G.number_of_nodes(),G.number_of_edges(),nodes[k],np.median(edmond),np.mean(edmond),np.std(edmond),np.var(edmond),nx.density(G))   
                Asign(dic, "dense","Dinitz", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(din),np.mean(din),np.std(din),np.var(din),nx.density(G))   
                Asign(dic, "dense","Boyk", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(boyk),np.mean(boyk),np.std(boyk), np.var(boyk),nx.density(G)) 
            G=AddEdges(nx.erdos_renyi_graph(size, 0.1))
            for k in range (5):
                edmond=[]
                din=[]
                boyk=[]
                for l in range(5):
                    edmond.append(Edmond(G,nodes[l][0],nodes[l][1]))
                    din.append(Din(G,nodes[l][0],nodes[l][1]))
                    boyk.append(Boyk(G,nodes[l][0],nodes[l][1]))
                Asign(dic, "erdos","Edmond", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(edmond),np.mean(edmond),np.std(edmond),np.var(edmond),nx.density(G))   
                Asign(dic, "erdos","Dinitz", G.number_of_nodes(),  G.number_of_edges(),nodes[k],np.median(din),np.mean(din),np.std(din),np.var(din),nx.density(G))   
                Asign(dic, "erdos","Boyk", G.number_of_nodes(),  G.number_of_edges(),nodes[k],np.median(boyk),np.mean(boyk),np.std(boyk),np.var(boyk),nx.density(G))   
            G=AddEdges(AddEdges(nx.random_tree(size)))
            for k in range (5):
                edmond=[]
                din=[]
                boyk=[]
                for l in range(5):
                    edmond.append(Edmond(G,nodes[l][0],nodes[l][1]))
                    din.append(Din(G,nodes[l][0],nodes[l][1]))
                    boyk.append(Boyk(G,nodes[l][0],nodes[l][1]))
                Asign(dic, "tree","Edmond", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(edmond),np.mean(edmond),np.std(edmond),np.var(edmond),nx.density(G))   
                Asign(dic, "tree","Dinitz", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(din),np.mean(din),np.std(din),np.var(din),nx.density(G))   
                Asign(dic, "tree","Boyk", G.number_of_nodes(), G.number_of_edges(),nodes[k],np.median(boyk),np.mean(boyk),np.std(boyk),np.var(boyk),nx.density(G))                                        
        size*=base;
    df=pd.DataFrame(dic)
    df.to_csv("matrix.csv") 
GenerateGraphs(100,2)
    

    