# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 02:35:09 2019

@author: lapi7
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
#df.groupby(['edges', ])
ANV=pg.anova (dv='mean_exec_time_log', between='algorithm', data=df, detailed=True)
pg.print_table (ANV)


ax=sns.boxplot(x=df["mean_exec_time_log"], y=df["algorithm"], data=df, palette="Set1")
tukey = pairwise_tukeyhsd(endog = df["mean_exec_time_log"],     # Data
                          groups= df["algorithm"],   # Groups
                          alpha=0.05)          # Significance level

tukey.plot_simultaneous(xlabel='Time', ylabel='algorithm')    # Plot group confidence intervals
plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")

print(tukey.summary())
plt.show()
