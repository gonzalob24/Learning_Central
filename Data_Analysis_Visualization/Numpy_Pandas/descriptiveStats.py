# -*- coding: utf-8 -*-

"""
Summary Statistics
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import datetime 
from numpy.random import randn
 
arr = np.array([[1,2, np.nan],[np.nan, 3, 4]])

dframe1 = DataFrame(arr, index=['A','B'], columns=['One','Two','Three'])

# summ ignores nan values, treats them as zero's
dframe1.sum()

# add up the rows
dframe1.sum(axis=1)

# finds the min value in each column
dframe1.min()

#index of each  min value
dframe1.idxmin()

# finding the max are the same methods just use max

# accumulation sum along the columns
dframe1.cumsum()


"""
Describe Method gives summary statistics
"""
dframe1.describe()

"""
Information on correlation and covariance
"""
from IPython.display import YouTubeVideo

play = YouTubeVideo('xGbpuFNR1ME')   # Covariance
play2 = YouTubeVideo('4EXNedimDMs')  # Correlation

prices = yf.download("CVX XOM BP", start="2010-01-01", end="2013-01-01")["Adj Close"]
prices.head()
volume = yf.download("CVX XOM BP", start="2010-01-01", end="2013-01-01")["Volume"]
volume.head()

# return is the % change in prices
returns = prices.pct_change()
corr = returns.corr
# plot the prices
prices.plot()

# plotting corr
sns.heatmap(returns)


"""
Missing Data
"""

data = Series(['one', 'two', np.nan, 'four'])

# Seing if a series has a null value
data.isnull()
# removing the nan values
data.dropna()

# In dataframe
dframe = DataFrame([[1,2,3], [np.nan,5,6], [7,np.nan,9], [np.nan,np.nan,np.nan]])

# If i drop nan value then i will only get the first row
clean_dframe = dframe.dropna()

# only drop rows that are missing all data
dframe.dropna(how='all')

# drop columns
dframe.dropna(axis=1)

# thresholdong the data
npn = np.nan
dframe2 = DataFrame([[1,2,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])

# threshold data points: only want rows that have at least 2 data points, for example.
dframe2.dropna(thresh=2)
dframe2.dropna(thresh=3)

# fill where nan values exist
dframe2.fillna(1)

# fill different values for diffrent columns by passing a dictionary 
dframe2.fillna({0:0, 1:1, 2:2, 3:3})

# modifies the data inplace without using equals sign
dframe2.fillna(0, inplace=True)



"""
Index Hierarchy
"""
# assigns index levels
ser = Series(randn(6), index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])

# checl multiple levels
ser.index
# calling the first index
ser[1]
ser[2]

# want to know all levels associates with a particulat index
ser[:, 'a']

# create dataframe from multipole levels
# levels are index and the indicies of the data are set as columns
dframe = ser.unstack()

# I can also construct a dataframe with multiple index levels
# the index's get matched up 
dframe2 = DataFrame(np.arange(16).reshape(4,4), index=[['a','a','b','b'],[1,2,1,2]],
                    columns=[['NY','NY','LA','SF'],['cold','hot','hot','cold']])


dframe2.index.names = ['INDEX_1','INDEX_2']
dframe2.columns.names = ['Cities','Temp']


# Swap levels this examples swaps Cities and Temp
dframe2.swaplevel('Cities', 'Temp', axis=1)


# Sort  by levels
dframe2.sort_index(level=1)

# perform operations by level
dframe2.sum(level='Temp', axis=1)

































