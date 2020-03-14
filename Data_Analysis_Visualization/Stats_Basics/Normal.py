#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:35:44 2020

@author: gonzalobetancourt
"""

#Import
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#Import the stats library
from scipy import stats

# Set the mean
mean = 0

#Set the standard deviation
std = 1


# Create a range
X = np.arange(-4,4,0.01)

#Create the normal distribution for the range
Y = stats.norm.pdf(X,mean,std)

#
plt.plot(X,Y)

#Set the mean and the standard deviaiton
mu,sigma = 0,0.1

# Now grab 1000 random numbers from the normal distribution
norm_set = np.random.normal(mu,sigma,1000)

import seaborn as sns

plt.hist(norm_set, bins=50)
