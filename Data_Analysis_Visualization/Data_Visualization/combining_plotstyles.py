#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:48:48 2020

@author: gonzalobetancourt
"""

import numpy as np
from numpy.random import randn
import pandas as pd

# Import the stats library from numpy
from scipy import stats

# These are the plotting modules and libraries I will use
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset = randn(100) # 100 points
sns.distplot(dataset, bins=25) # default bins are set to 10

sns.distplot(dataset, rug=True, hist=True, bins=25) 

sns.distplot(dataset, kde_kws={'color':'red', 'label':'KDE PLOT'}, 
                          hist_kws={'color':'blue', 'label':'HIST'}, bins=25) 

ser1 = pd.Series(dataset, name='My Data')
sns.distplot(ser1, bins=25)


#########3 Box and Viloin Plots ###############

# PDF Functions

data1 = randn(100)
data2 = randn(100)


sns.boxplot(data1)
sns.boxplot([data1, data2], whis=np.inf)


#  normal distribution
data3 = stats.norm(0,5).rvs(100)

# Two gamma distributions. Concatenated together

data4 = np.concatenate([stats.gamma(5).rvs(50)-1,
                        -1*stats.gamma(5).rvs(50)])
sns.boxplot([data2, data4])

# KDE with box plot
sns.violinplot(data3, bw=0.01,split=True)