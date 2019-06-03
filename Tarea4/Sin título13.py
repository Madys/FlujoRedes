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

df = pd.read_csv("Matrix.csv", dtype={ "Densidad": np.float64 })
logX = np.log1p(df["Mediana"])
df = df.assign(mediana=logX.values)
df.drop(["Mediana"], axis= 1, inplace= True)

for i in range(0, df["Densidad"].count()):
    if  df.iat[i, 9]  < 0.03716667:
        df.iat[i, 9] = 1    
    elif df.iat[i, 9]  < 0.07183333:        
        df.iat[i, 9] = 2
    else:       
        df.iat[i, 9] = 3

df["Densidad"].replace({1: '1 baja', 2: '2 media', 3: '3 alta'}, inplace= True)          
plt.figure(figsize=(8, 6))   
model_name = ols('mediana ~ Generador+Algoritmo+Nodos+Densidad+Generador*Algoritmo+Algoritmo*Nodos+Nodos*Densidad+Generador*Nodos+Generador*Densidad+Algoritmo*Densidad', data=df).fit()
model_name.summary()
aov_table = sm.stats.anova_lm(model_name, typ=2)
df1=pd.DataFrame(aov_table)
df1.to_csv("new.csv")  
print(model_name)
