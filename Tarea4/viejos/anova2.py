# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:26:43 2019

@author: lapi7
"""

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import numpy as np

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison



df = pd.read_csv("Parameterized_dataset_OQ7E9S7KML_2019_3_18_5_18_58_44431.csv", index_col=None )
df.drop(['run', 'iterations'], axis= 1, inplace= True)
print(rp.summary_cont(df['mean_exec_time']))

logX = np.log10(df['mean_exec_time'])
print(logX)
df = df.assign(mean_exec_time_log=logX.values)
print(df)
df.drop(['mean_exec_time'], axis= 1, inplace= True)
print(df)

print(rp.summary_cont(df['mean_exec_time_log'].groupby(df['algorithm'])))

results = ols('mean_exec_time_log ~ C(algorithm)', data=df).fit()
print (results.summary())

aov_table = sm.stats.anova_lm(results, typ=2)
print(aov_table)

#hacer un boxplot!! para visualizar lo obtenido del anova

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

bc=df[ (df['algorithm']=='betweenness_centrality')]
gc=df[ (df['algorithm']=='greedy_color')]
dfs=df[ (df['algorithm']=='dfs_tree')]

print(bc)
ax=sns.boxplot(x=df["mean_exec_time_log"], y=df["algorithm"],  data=df, palette="Set1")
ax=sns.swarmplot(x=df["mean_exec_time_log"], y=df["algorithm"],  data=df, color="black")
fig.savefig('fig1.png', bbox_inches='tight')
plt.show()

mc = MultiComparison(df['mean_exec_time_log'], df['algorithm'])
mc_results = mc.tukeyhsd()
print(mc_results)

