#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:46:37 2020

@author: gonzalobetancourt
"""
import numpy as np
from numpy.random import randn
import pandas as pd

# stats library
from scipy import stats

# plotting modules and libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


dataset = randn(25)

sns.rugplot(dataset)
plt.ylim(0,0.02)

# counts number of ticks per bin
plt.hist(dataset,alpha=0.3)
sns.rugplot(dataset)

sns.rugplot(dataset)
x_min = dataset.min() - 2
x_max = dataset.max() + 2
# 100 equally spaced points fom min to max
x_axis = np.linspace(x_min, x_max, 100)

# bandwidth estimation, is a standard equation
bandwidth = ((4 * dataset.std()**5) / (3*len(dataset))) ** 0.2 

kernel_list = []

for data_point in dataset:
    #create a kernel for each point an append it to the kernal_list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    # Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * 0.4
    
    plt.plot(x_axis, kernel, color='gray', alpha=0.5)

plt.ylim(0,1)

# kernel density estimation will be the sum
sum_of_kde = np.sum(kernel_list, axis=0)
fig = plt.plot(x_axis, sum_of_kde, color='indianred')
sns.rugplot(dataset)
plt.yticks([])
plt.suptitle("Sum of the basis functions")

# This is the easy way using seaborn
sns.kdeplot(dataset)

sns.rugplot(dataset, color="black")
for bw in np.arange(0.5,2,0.25):
    sns.kdeplot(dataset, bw=bw, lw=1.8, label=bw)
    

kernel_options = ['biw', 'cos', 'epa', 'gau', 'tri', 'triw']

for kern in kernel_options:
    sns.kdeplot(dataset, kernel=kern, label=kern, shade=True)
    
# CDF
sns.kdeplot(dataset, cumulative=True)

# multivariate density

mean = [0,0]

cov = [[1,0],[0,100]]

ds = np.random.multivariate_normal(mean, cov, 1000)

dframe = pd.DataFrame(ds, columns=['X', 'Y'])
sns.kdeplot(ds, shade=True)

sns.kdeplot(ds, bw=bw)

sns.kdeplot(ds, bw='silverman')
    
# kde joint polot
sns.jointplot('X','Y', dframe, kind='kde')    
    
    
    
    
    
    
    