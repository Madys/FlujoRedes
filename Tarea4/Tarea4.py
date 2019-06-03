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
  
def AddEdges(S):
    scale = 2
    rang = 10
    size = S.number_of_edges()  
    e=S.edges(nbunch=None, data=True, default=None)   
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)
    G=nx.Graph()
    count=0;
    for i in e:
        G.add_edge(i[0],i[1],capacity=X[count]+rang+1)
        count+=1
    return G

def RandNodes(maxi):
    a=rdm.randint(1,maxi) 
    b=rdm.randint(1,maxi)  
    while a==b:
        b=rdm.randint(1,maxi)
    return [a,b]
    
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

def GenerateDic(size,base):   
    dic={}
    for i in range(1,5):  
        for j in ["dupl","fast","comp"]:          
            for k in ["Edmond","Din","Boyk"]:
                dic[k+str(size)+j]=[]
        size*=base
    return dic
                    
def GenerateGraphs(size, base):
    numNodes={"fast":[],"dupl": [],"comp":[]}
    dic=GenerateDic(size,base)
    for i in range(1,5):  
        print("ciclo"+str(i))
        for j in range(10):        
#           G=AddEdges(nx.fast_gnp_random_graph(size, 0.5)) 
            G=AddEdges(nx.dense_gnm_random_graph(size,int(size*size*0.2 )))     
            numNodes["fast"].append([G.number_of_edges,size])
            print("fast"+str(j))
            for k in range (5):
                nodes=RandNodes(size-1)              
                for l in range(5):
                    dic["Edmond"+str(size)+"fast"].append(Edmond(G,nodes[0],nodes[1]))                    
                    dic["Din"+str(size)+"fast"].append(Din(G,nodes[0],nodes[1]))    
                    dic["Boyk"+str(size)+"fast"].append(Boyk(G,nodes[0],nodes[1]))
            G=AddEdges(nx.duplication_divergence_graph(size, 0.2))
            numNodes["dupl"].append([G.number_of_edges,size])
            print("dupl"+str(j))
            for k in range (5):
                nodes=RandNodes(size-1)
                for l in range(5):
                    dic["Edmond"+str(size)+"dupl"].append(Edmond(G,nodes[0],nodes[1]))
                    dic["Din"+str(size)+"dupl"].append(Din(G,nodes[0],nodes[1]))    
                    dic["Boyk"+str(size)+"dupl"].append(Boyk(G,nodes[0],nodes[1]))   
            G=AddEdges(nx.complete_graph(size))
            numNodes["comp"].append([G.number_of_edges,size])
            print("comp"+str(j))
            for k in range (5):
                nodes=RandNodes(size-1)
                for l in range(5):
                    dic["Edmond"+str(size)+"comp"].append(Edmond(G,nodes[0],nodes[1]))
                    dic["Din"+str(size)+"comp"].append(Din(G,nodes[0],nodes[1]))    
                    dic["Boyk"+str(size)+"comp"].append(Boyk(G,nodes[0],nodes[1]))            
        size*=base;
    df=pd.DataFrame(dic)
    df.to_csv("matrix.csv") 
    df=pd.DataFrame(numNodes)
    df.to_csv("Nodes.csv") 
GenerateGraphs(20,2)
