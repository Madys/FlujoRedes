# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:42:06 2019

@author: Madys
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pingouin as pg
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import csv
df = pd.read_csv("Todos.csv", index_col=None, usecols=[4,6,7,8,9,10,11,12],dtype={ 'Flujomaximo': np.int,'Mediana': np.float64, 'Grado': np.int, 'CoefA':np.float64, 'CentCe': np.float64,'CentCa': np.float64,
                                                                        'Excent': np.int,'PageR': np.float64} )

modelo = ols('Flujomaximo ~ Grado+CoefA+CentCe+CentCa+Excent+PageR+Grado*CoefA+Grado*CentCe+Grado*CentCa+Grado*Excent+Grado*PageR+CentCe*CentCa+CentCe*Excent+CentCe*PageR+CentCa*Excent+CentCa*PageR+Excent*PageR',data=df).fit()
print(modelo.summary())
modelo_csv = open("Anova_Mult.csv", 'w')
aov_table = sm.stats.anova_lm(modelo, typ=2)
df1=pd.DataFrame(aov_table)
df1.to_csv("modeloflujo.csv")


for i in range(0, df["Grado"].count()):
    if  df.iat[i, 2]  < 3:
        df.iat[i, 2] = 1    
    elif df.iat[i,2]  < 5:        
        df.iat[i, 2] = 2
    else:       
        df.iat[i, 2] = 3

  
df["Grado"].replace({1: "baja", 2: "media", 3: "alta"}, inplace= True)
print(df["CoefA"])
for i in range(0, df["CoefA"].count()):
    if  df.iat[i, 3]  < 0.3333:
        df.iat[i, 3] = 1    
    elif df.iat[i, 3]  < 0.66667:        
        df.iat[i, 3] = 2
    else:       
        df.iat[i, 3] = 3

   
df["CoefA"].replace({1: "baja", 2: "media", 3: "alta"}, inplace= True)
for i in range(0, df["CentCe"].count()):
    if  df.iat[i, 4]  < 0.3868:
        df.iat[i, 4] = 1    
    elif df.iat[i,4 ]  < 0.4813:        
        df.iat[i, 4] = 2
    else:       
        df.iat[i, 4] = 3
    
df["CentCe"].replace({1: "baja", 2: "media", 3: "alta"}, inplace= True)
for i in range(0, df["CentCa"].count()):
    if  df.iat[i, 5]  < 0.08173333:
        df.iat[i, 5] = 1    
    elif df.iat[i,5]  < 0.16346667:        
        df.iat[i, 5] = 2       
    else:       
        df.iat[i, 5] = 3

   
df["CentCa"].replace({1: "baja", 2: "media", 3: "alta"}, inplace= True)
for i in range(0, df["Excent"].count()):
    if  df.iat[i, 6]  < 3.66:
        df.iat[i,6] = 1    
    elif df.iat[i,6]  < 4.33:        
        df.iat[i, 6] = 2
    else:       
        df.iat[i,6] = 3
     
df["Excent"].replace({1: "baja", 2: "media", 3: "alta"}, inplace= True)
for i in range(0, df["PageR"].count()):
    if  df.iat[i, 7]  < 0.042296667:
        df.iat[i, 7] = 1    
    elif df.iat[i,7]  < 0.0673333:        
        df.iat[i, 7] = 2
    else:       
        df.iat[i,7] = 3
    
df["PageR"].replace({1: "baja", 2: "media", 3: "alta"}, inplace= True)


#logX = np.log10(df['Mediana'])
#df = df.assign(mediana_log=df['Mediana'])
#df.drop(['Mediana'], axis= 1, inplace= True)

factores=["Grado","CoefA","CentCe","CentCa","Excent","PageR"]
plt.figure(figsize=(8, 6))
for i in factores:
    anova = pg.anova (dv=df["Flujomaximo"], between=i, data=df, detailed=True  )
    pg._export_table (anova,("ANOVAs"+i+".csv"))
    ax=sns.boxplot(x=df["Flujomaximo"], y=df[i], data=df, palette="cubehelix")
    plt.savefig("boxflujo" + i + ".eps", bbox_inches='tight')
    tukey = pairwise_tukeyhsd(endog = df["Flujomaximo"], groups= df[i], alpha=0.05)
    tukey.plot_simultaneous(xlabel='Flujo máximo', ylabel=i)
    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
    plt.savefig("simultaneous_flujo" + i + ".eps", bbox_inches='tight')
    print(tukey.summary())
    t_csv = open("Tukeyflujo"+i+".csv", 'w')
    with t_csv:
        writer = csv.writer(t_csv)
        writer.writerows(tukey.summary())
    plt.show()