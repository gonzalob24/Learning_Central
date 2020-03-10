#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:13:03 2020

@author: gonzalobetancourt
"""

# Discrete Uniform Distributions

# Definition: A random variable X has a discrete uniform distribution if 
# each of the n values in its range: x1,x2,x3....xn has equal probability:

# f(x) = 1/n
# Import all the usual imports from the Python for Data Analysis and Visualization Course.

from __future__ import division
import numpy as np
from numpy.random import randn
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# Now let's set up a dice roll and plot the distribution using seaborn before 
# we go use matplotlib by itself.

# A dice roll

# The Probability Mass function

# Each number
roll_options = [1,2,3,4,5,6]

# Total probability space is 1
tprob = 1

# Each roll has the same odds of appearing --> 1/6
prob_roll = tprob / len(roll_options)

# Plot using seaborn rugplot (note this is not really a rugplot), 
# setting height equal to probability of roll
uni_plot = sns.rugplot(roll_options, height=prob_roll, c='indianred')

# Set Title
uni_plot.set_title('Probability Mass Function for Dice Roll')

# We can see in the above example that the f(x) value on the plot is just 
# equal to 1/(Total Possible Outcomes)


# The mean is simply the max and min value divided by two, just like 
# the mean of two numbers     μ=(b+a)/2
# With a variance of:  σ^2=(b−a+1)^2 / 12
 
# automatically create a Discrete Uniform Distribution using Scipy.
# Imports
from scipy.stats import randint

#Set up a low and high boundary for dice roll ( go to 7 since index starts at 0)
low,high = 1,7

# Get mean and variance
mean,var = randint.stats(low,high)

print("The mean is {}".format(mean))
print("The Variance is {}".format(var))

plt.bar(roll_options,randint.pmf(roll_options,low,high))


# Population max = sample max + (sample max / sample size) −1
 






























