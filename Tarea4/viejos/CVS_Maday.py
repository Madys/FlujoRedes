# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:09:09 2019

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
#from lsdhotest.py import LSD(response_to_treatments, probability)
#import spm1d.stats.anova3 as sp

df = pd.read_csv("matrix.csv", index_col=None )
logX = np.log10(df['Average'])
print(logX)
df = df.assign(Average_log=logX.values)
print(df)
df.drop(['Average'], axis= 1, inplace= True)
print(df)

ax=sns.boxplot(x=df["Average_log"], y=df["Edges"], data=df, palette="Set1")
tukey = pairwise_tukeyhsd(endog = df["Average_log"],     # Data
                          groups= df["Edges"],   # Groups
                          alpha=0.05)          # Significance level

tukey.plot_simultaneous(xlabel='Time', ylabel='Edges')    # Plot group confidence intervals
plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
#fig.savefig('fig1.png', bbox_inches='tight')
print(tukey.summary())
plt.show()

#vind=[df["Generator"],df["Algorithm"]]
#d=pg.rm_anova2 ( dv = "Average_log" , within = ["Generator","Algorithm"] , subject="Edges", data = df , 
#                   export_filename = "multianova.csv")
#
#pg.print_table (d)

#d=sp( df["Average_log"] , df["Generator"] , df["Algorithm"] , df["Edges"] , equal_var = True , roi = None )