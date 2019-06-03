from __future__ import print_function
from statsmodels.compat import urlopen
import numpy as np
np.set_printoptions(precision=4, suppress=True)
import statsmodels.api as sm
import pandas as pd
pd.set_option("display.width", 100)
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm

df = pd.read_csv('Matrix.csv', index_col=None,usecols=[1,2,3,4,8], dtype={'Nodos': 'category', "Densidad": np.float64 })
for i in range(0, df["Densidad"].count()):
    if  df.iat[i, 9]  < 0.03716667:
        df.iat[i, 9] = 1    
    elif df.iat[i, 9]  < 0.07183333:        
        df.iat[i, 9] = 2
    else:       
        df.iat[i, 9] = 3
df["Densidad"].replace({1: '1 baja', 2: '2 media', 3: '3 alta'}, inplace= True)    
     
Generador = df["Generador"]
Algoritmo = df["Algoritmo"]
Nodos = df["Nodos"]
Densidad = df["Densidad"]

plt.figure(figsize=(6,6))
symbols = ['D', '^']
colors = ['r', 'g', 'blue']
factor_groups = df.groupby(['Generador','Algoritmo'])
for values, group in factor_groups:
    i,j = values
    plt.scatter(group['Nodos'], group['Densidad'], marker=symbols[j], color=colors[i-1],
               s=144)
plt.xlabel('Experience');
plt.ylabel('Salary');
