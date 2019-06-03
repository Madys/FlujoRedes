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

df = pd.read_csv("Matrix.csv", index_col=None )

logX = np.log1p(df["Average"])
df = df.assign(media_log=logX.values)
df.drop(["Average"], axis= 1, inplace= True)
df["Generator"]
factores=["Generator"]
plt.figure(figsize=(8, 6))
for i in factores:
    print(rp.summary_cont(df['media_log'].groupby(df[i])))
    ANV=pg.anova (dv='media_log', between=i, data=df, detailed=True)
    pg.print_table (ANV)

    ax=sns.boxplot(x=df["media_log"], y=df[i], data=df, palette="Set1")
    tukey = pairwise_tukeyhsd(endog = df["media_log"],     # Data
                          groups= df[i],   # Groups
                          alpha=0.05)          # Significance level
    plt.savefig('fig1.jpeg', bbox_inches='tight')
    tukey.plot_simultaneous(xlabel='Time', ylabel=i)    # Plot group confidence intervals
    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
    plt.savefig('fig2.jpeg', bbox_inches='tight')
    print(tukey.summary())
    plt.show()