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

def GenerateGraph(nameToSave,Smin,Smax,max_weight,numberOfGraphs):
    for h in range(numberOfGraphs):
        G=nx.Graph()
        size=rdm.randint(Smin,Smax)
        for i in range(size):
            for j in range(i, size):        
                if rdm.randint(0,int(size/20))==0:
                    G.add_edge(i,j, weight=rdm.randint(1,max_weight))  
        df = pd.DataFrame()
        df = nx.to_pandas_adjacency(G, dtype=int, weight='weight')
        df.to_csv(nameToSave+str(h)+".csv")

def GenerateDiGraph(nameToSave,Smin,Smax,max_weight,numberOfGraphs):
    for h in range(numberOfGraphs):
        G=nx.DiGraph()
        size=rdm.randint(Smin,Smax)
        for i in range(size):
            for j in range(i, size):        
                if rdm.randint(0,int(size/50))==0:
                    G.add_edge(i,j, weight=rdm.randint(1,max_weight))  
                elif rdm.randint(0,int(size/30))==1:
                    G.add_edge(j,i, weight=rdm.randint(1,max_weight))         
        df = pd.DataFrame()
        df = nx.to_pandas_adjacency(G, dtype=int, weight='weight')
        df.to_csv(nameToSave+str(h)+".csv")
   
def ReadGraph(adress):
    ds = pd.read_csv(adress, header=None)
    G = nx.from_pandas_adjacency(ds)
    return G

def ReadDiGraph(adress):
    ds = pd.read_csv(adress,header=None)
    G = nx.from_pandas_adjacency(ds,create_using=nx.DiGraph())
    return G

def PrintImage(G):
    pos = nx.spectral_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=60, node_color='b', node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1, edge_color='black')
    edge_labels=nx.draw_networkx_edge_labels(G,pos,font_size=7,label_pos=.5)

def BetCen(graph):
    start_time=time()        
    R = nx.betweenness_centrality(graph, weight= 'size', normalized=False)
    time_elapsed = time() - start_time  
    return time_elapsed
    
def MinMaxMat(graph):
    start_time=time()  
    for i in range (100):      
        R = nx.maximal_matching(graph)
    time_elapsed = time() - start_time  
    return time_elapsed

def GreedyColor(graph):
    start_time=time() 
    for i in range (160):                     
        R = nx.greedy_color(graph, strategy='largest_first', interchange=False)
    time_elapsed = time() - start_time  
    return time_elapsed

def MaxClique(graph):
    start_time=time()          
    R = nx.make_max_clique_graph(graph, create_using=None)
    time_elapsed = time() - start_time  
    return time_elapsed

def StronglyC(graph):
    start_time=time() 
    for i in range(99000):       
        R = nx.strongly_connected_components(graph)
    time_elapsed = time() - start_time  
    return time_elapsed

matrix = {
            '0': [],
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': [],
            '9': [],
            '10': [],
            '11': [],
            '12': [],           
            '13': [],
            '14': [],
            '15': [],
            '16': [],
            '17': [],           
            '18': [],
            '19': [],
            '20': [],
            '21': [],
            '22': [],           
            '23': [],
            '24': [],       
        }
  
def RunAll(runs,numAlgorithms,numGraphs,name,nameDi,matrix):
    combinations=[]
    for i in range(numAlgorithms-1):
        for j in range (numGraphs):        
            combinations.append([i,name+str(j)+".csv"])           
    for j in range (numGraphs):        
        combinations.append([numAlgorithms-1,nameDi+str(j)+".csv"])
    for j in range(runs):
        np.random.shuffle(combinations)
        for i in combinations:             
            if i[0]==0:
                for n in range(numGraphs):
                    if i[1]==name+str(n)+".csv":
                        matrix[str(n)].append(BetCen(ReadGraph(i[1])))                         
            if i[0]==1:
                for n in range(numGraphs):
                    if i[1]== name+str(n)+".csv":
                        matrix[str(n+5)].append(MinMaxMat(ReadGraph(i[1])))                            
            if i[0]==2:
                for n in range(numGraphs):
                    if i[1]== name+str(n)+".csv":
                       matrix[str(n+10)].append(GreedyColor(ReadGraph(i[1])))     
            if i[0]==3:
                for n in range(numGraphs):
                    if i[1]== name+str(n)+".csv":
                       matrix[str(n+15)].append(MaxClique(ReadGraph(i[1])))    
            if i[0]==4:
                for n in range(numGraphs):
                    if i[1]== "directed"+str(n)+".csv":
                       matrix[str(n+20)].append(StronglyC(ReadDiGraph(i[1])))                    
    df = pd.DataFrame(matrix)
    df.to_csv("matrix.csv")
                                                            
def MediaDesv (adress,runs,numberOfGraphs,numAlgorithms,name,nameDi):   
    media = {
            'Media0': [],
            'Media1': [],
            'Media2': [],
            'Media3': [],
            'Media4': [],         
             }
    standar={'Standar0': [],
            'Standar1': [],   
            'Standar2': [],   
            'Standar3': [],
            'Standar4': [],
            }    
    grafos={
            'EdgesUndirected':[],
            'NodesUndirected':[],
            'EdgesDirected':[],
            'NodesDirected':[]
            }   
    matrix = pd.read_csv(adress)
    for n in range(5):
        grafos['EdgesUndirected'].append(ReadGraph (name+str(n)+".csv").number_of_edges())
        grafos['NodesUndirected'].append(ReadGraph (name+str(n)+".csv").number_of_nodes())
        grafos['EdgesDirected'].append(ReadGraph (nameDi+str(n)+".csv").number_of_edges())
        grafos['NodesDirected'].append(ReadGraph (nameDi+str(n)+".csv").number_of_nodes())
        for i in range(5):
            media['Media'+str(i)].append(np.mean(matrix[str(n+(5*i))])) 
            standar['Standar'+str(i)].append(np.std(matrix[str(n+(5*i))]))                      
    df=pd.DataFrame(media)
    df.to_csv("Media.csv", index=None) 
    df=pd.DataFrame(standar,)
    df.to_csv("Standar.csv", index=None) 
    df=pd.DataFrame(grafos)
    df.to_csv("Grafos.csv", index=None) 

def Histograma(adress):
    df = pd.read_csv(adress)
    nrows=2
    ncols=3
    fig,axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 10))  
    counter = 0
    for i in range(nrows):
        for j in range(ncols):   
            ax = axes[i][j]    
            if counter < len(df.columns):    
                ax.hist(df[df.columns[counter]], bins=5, color='red', alpha=0.8, label='{}'.format(df.columns[counter]))
                ax.set_xlabel('Valores')
                ax.set_ylabel('Ocurrencia')
                ax.set_ylim([0, 5])
                leg = ax.legend(loc='upper left')
                leg.draw_frame(False)  
            else:
                ax.set_axis_off()   
            counter += 1  
    plt.savefig("histograma.eps")

def ScatterNodes(media,nodos,standar):
    colors = ["y","r","b","black","g"] 
    media = pd.read_csv(media)
    nodes=pd.read_csv(nodos)
    standar=pd.read_csv(standar)
    markers=["d","o","*",">","X"]   
    for i in range(4):
        x=media["Algoritmo"+str(i)]
        area=300
        p = pd.read_csv(nodos)
        y=nodes["NodesUndirected"]
        plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker=markers[i])    
    x=media["Algoritmo"+str(4)]
    area=300
    p = pd.read_csv(nodos)
    y=nodes["NodesDirected"]
    plt.xlabel('Tiempo promedio de ejecución')
    plt.ylabel('Cantidad de nodos')
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker=markers[4])    
    plt.savefig("scatterNodes.eps")
    plt.savefig("scatterNodes.jpeg")
   
def ScatterEdges(media,edges,standar):
    colors = ["y","r","b","black","g"] 
    media = pd.read_csv(media)
    nodes=pd.read_csv(edges)
    standar=pd.read_csv(standar)
    markers=["d","o","*",">","X"]   
    for i in range(4):
        x=media["Algoritmo"+str(i)]
        area=300
        p = pd.read_csv(edges)
        y=nodes["EdgesUndirected"]
        plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker=markers[i])    
    x=media["Algoritmo"+str(4)]
    area=300
    plt.xlabel('Tiempo promedio de ejecución')
    plt.ylabel('Cantidad de aristas')
    p = pd.read_csv(edges)
    y=nodes["EdgesDirected"]
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, marker=markers[4]) 
    plt.xlabel('Tiempo promedio de ejecución')
    plt.ylabel('Cantidad de aristas')
    plt.savefig("scatterEdges.eps")
    plt.savefig("scatterEdges.jpeg")
    
#  Boxplots
#to_plot=[a1_t1_times,a1_t2_times,a1_t3_times,a1_t4_times,a1_t5_times]
#fig=plt.figure(1,figsize=(9,6))
#ax=fig.add_subplot(111)
#bp=ax.boxplot(to_plot, showfliers=False)
#plt.xlabel('Grafo')
#plt.ylabel('Tiempo (segundos)')
#plt.title('Ruta más corta')
#plt.savefig('BP1.eps', format='eps', dpi=1000)
#plt.show()

name="undirected"
nameDi="directed"
Smin=250
Smax=400
SminDi=1000
SmaxDi=1500
max_weight=8
numberOfGraphs=5
numAlgorithms=5
runs=20

#GenerateGraph(name,Smin,Smax, max_weight, numberOfGraphs)
#GenerateDiGraph(nameDi,SminDi,SmaxDi, max_weight, numberOfGraphs)
#RunAll(runs, numAlgorithms, numberOfGraphs, name,nameDi, matrix)
#MediaDesv ("matrix.csv",runs,numberOfGraphs,numAlgorithms,name,nameDi) 
#Histograma("Media.csv")
#ScatterNodes("Media.csv","Grafos.csv","Standar.csv")
ScatterEdges("Media.csv","Grafos.csv","Standar.csv") 
