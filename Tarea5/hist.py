# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:18:15 2019

@author: Madys
"""

from statsmodels.formula.api import ols
import numpy as np
import pingouin as pg
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import csv

df = pd.read_csv("Todos.csv")
#, dtype={'Nodos': 'category', 'Generados': 'category',"Densidad": np.float64 }
#logX = np.log1p(df["Mediana"])
#df = df.assign(mediana=logX.values)
#df.drop(["Mediana"], axis= 1, inplace= True)

for i in range(0, df["CoefA"].count()):
    if  df.iat[i, 8]  < 0.2:
        df.iat[i, 8] = 1    
    elif df.iat[i, 8]  < 0.4:        
        df.iat[i, 8] = 2
    elif df.iat[i, 8]  < 0.6:      
        df.iat[i, 8] = 3
    elif df.iat[i, 8]  < 0.8:         
        df.iat[i, 8] = 4
    else:       
        df.iat[i, 8] = 5
        
df["CoefA"].replace({1: "muy baja", 2: "baja", 3: "media", 4: "alta",5: "muy alta"}, inplace= True)          
#factores=["Nodos","Generador","Algoritmo","Densidad"]
#for i in factores:
#    print(rp.summary_cont(df['mediana'].groupby(df[i])))
#    anova = pg.anova (dv='mediana', between=i, data=df, detailed=True , )
#    pg._export_table (anova,("ANOVA"+i+".csv"))
#    ax=sns.boxplot(x=df["mediana"], y=df[i], data=df, palette="Set1")
#    plt.savefig(i+"1.png", bbox_inches='tight')
#    plt.savefig( i + "1.eps", bbox_inches='tight')
#    tukey = pairwise_tukeyhsd(endog = df["mediana"], groups= df[i], alpha=0.05)
#    tukey.plot_simultaneous(xlabel='Time', ylabel=i)
#    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
#    plt.savefig(i+"2.png", bbox_inches='tight')
#    plt.savefig(i + "2.eps", bbox_inches='tight')
#    t_csv = open("Tukey"+i+".csv", 'w')
#    with t_csv:
#        writer = csv.writer(t_csv)
#        writer.writerows(tukey.summary())
#    plt.show()