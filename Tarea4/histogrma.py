# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:09:57 2019

@author: Madys
"""
import matplotlib.pyplot as plt


def Histograma(adress):
    df = pd.read_csv(adress, usecols=[10])                  
    df = pd.read_csv(adress)
    his=plt.hist(round(df["Densidad"],4),bins=3)
    print(his)
    plt.xlabel("Densidad")
    plt.ylabel("Cantidad de valores")
    plt.savefig("HistoDens.eps")
Histograma("Matrix.csv")