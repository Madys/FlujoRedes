#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:20:09 2019

@author: hectorgarcia
"""

import numpy as np
import networkx as nx
from time import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from statsmodels.formula.api import ols
import statsmodels.api as sm


i=0
orden=[20,30,40,50,60]
datos=np.arange(sum(orden)*12, dtype=float).reshape(sum(orden),12)
fila=0

#----------------------------------Gráficos------------------------------------
                  #-----Visualizar Fuente y Sumidero-------
H=nx.watts_strogatz_graph(orden[i], int(orden[i]/2) , 0.33 , seed=None)

lista=[]
lista[:]=H.edges
width=np.arange(len(lista)*1,dtype=float).reshape(len(lista),1)
for r in range(len(lista)):
    R=np.random.normal(loc=20, scale=5.0, size=None)
    width[r]=R
    H.add_edge(lista[r][0],lista[r][1],capacity=R)
for w in range(10):  
    initial=random.randint(0,round(len(H.nodes)/2))
    final=random.randint(initial,len(H.nodes)-2)
    while initial==final:
        initial=random.randint(0,round(len(H.nodes)/2))
        final=random.randint(initial,len(H.nodes)-2)
    T=nx.maximum_flow(H, initial, final)
                        #-------Flujo------
    lista_flujo=[]
    for t in T[1].keys():
        for m in T[1][t].keys():
            print(T[1][t][m])
            if T[1][t][m]!=0:
                lista_flujo.append((t,m))
    edges = H.edges()
    weights = [(H[u][v]['capacity'])/15 for u,v in edges]     
    pos1=[initial,final]
    pos=nx.circular_layout(H)
    nx.draw(H, pos, node_color="white", node_size=800, with_labels=True, font_weight="bold", edgecolors="black")
    nx.draw_networkx_edges(H, pos, edgelist=lista_flujo, width=weights, edge_color='blue', style='solid')
    nx.draw_networkx_nodes(H, pos, pos1, node_color="red", node_size=800, with_labels=True, font_weight="bold", edgecolors="black")
    
    
#-------------------------------Experimentacion--------------------------------

for i in range(len(orden)):
    H=nx.watts_strogatz_graph(orden[i], int(orden[i]/2) , 0.33 , seed=None)
    pos=nx.circular_layout(H)
    nx.draw(H, pos, node_color="white", node_size=800, with_labels=True, 
            font_weight="bold", edgecolors="black")
    
    initial=0
    final=0
    lista=[]
    lista[:]=H.edges
    width=np.arange(len(lista)*1,dtype=float).reshape(len(lista),1)
    for r in range(len(lista)):
        R=np.random.normal(loc=20, scale=5.0, size=None)
        width[r]=R
        H.add_edge(lista[r][0],lista[r][1],capacity=R)
    for w in range(orden[i]):  
        initial=random.randint(0,round(len(H.nodes)/2))
        final=random.randint(initial,len(H.nodes)-2)
        while initial==final:
            initial=random.randint(0,round(len(H.nodes)/2))
            final=random.randint(initial,len(H.nodes)-2)
        tiempo_inicial=time()
        T=nx.maximum_flow(H, initial, final)
        tiempo_final=time()
        datos[fila,0]=T[0]
        datos[fila,1]=tiempo_final-tiempo_inicial
#---------------------------Info Fuente--------------------------------------
        datos[fila,2]=nx.clustering(H, nodes=initial)
        datos[fila,3]=nx.closeness_centrality(H, u=initial)
        datos[fila,4]=nx.load_centrality(H, v=initial)
        datos[fila,5]=nx.eccentricity(H, v=initial)
        datos[fila,6]=nx.pagerank(H, alpha=0.9)[initial]
#---------------------------Info Sumidero--------------------------------------
        datos[fila,7]=nx.clustering(H, nodes=final)
        datos[fila,8]=nx.closeness_centrality(H, u=final)
        datos[fila,9]=nx.load_centrality(H, v=final)
        datos[fila,10]=nx.eccentricity(H, v=final)
        datos[fila,11]=nx.pagerank(H, alpha=0.9)[final]
        fila+=1



data=datos.copy()
data=pd.DataFrame(data)
data.columns=['F.O.','Tiempo','Clstr_fuente','Clsns_fuente','Load_fuente','Ex_fuente','Prank_fuente','Clstr_sumidero','Clsns_sumidero','Load_sumidero','Ex_sumidero','Prank_sumidero'] 

#----------------------------------Correlación---------------------------------

corr = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='RdBu', vmin=-1, vmax=1, aspect='equal', origin='upper')
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
#plt.xticks(rotation=0)
#ax.set_yticks(ticks)
#ax.set_xticklabels(('Genera.', 'Algorit.', 'Orden', 'Densidad','Tiempo'))
#ax.set_yticklabels(('Generador', 'Algoritmo', 'Orden', 'Densidad','Tiempo'))
plt.title('Matriz Correlaciones',pad=16.0, size=14)
plt.savefig('Correlaciones1.eps', format='eps', dpi=1000,bbox_inches='tight')

#----------------------------------Box plot---------------------------------

data1= data[data['Generador'] == 0]
data2= data2[data2['Generador'] == 1]
data3= data2[data2['Generador'] == 2]

tiempos1= data4['Tiempo']
tiempos2= data5['Tiempo']
tiempos3= data6['Tiempo']


to_plot=[tiempos1, tiempos2, tiempos3]
fig=plt.figure(1,figsize=(9,6))
ax=fig.add_subplot(111)
bp=ax.boxplot(to_plot)
plt.ylim(-1,20)
plt.xlabel('Generador de grafo', size=14)
plt.ylabel('Tiempo (segundos)', size=14)
plt.title('Generador contra tiempo',size=18)
plt.savefig('boxplotgenerador.eps', format='eps', dpi=1000)

model_name = ols('F.O. ~ Generador+Algoritmo+Orden+Densidad+Generador*Algoritmo+Algoritmo*Orden+Orden*Densidad+Generador*Orden+Generador*Densidad+Algoritmo*Densidad+Generador*Algoritmo*Orden+Generador*Algoritmo*Densidad*Algoritmo*Orden*Densidad+Generador*Orden*Densidad', data=data2).fit()
f = open('Ols1.txt', "w")
f.write('%s \t' %model_name.summary())
f.close()

aov_table = sm.stats.anova_lm(model_name, typ=2)
f = open('Anova1.txt', "w")
f.write('%s \t' %aov_table)
f.close()










