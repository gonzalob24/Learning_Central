
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html
from io import StringIO

import sys
import json



"""
Group by
"""

df = DataFrame({'k1':['X','X','Y','Y','Z'],
                'k2':['alpha','beta','alpha','beta','alpha'],
                'dataset1':np.random.randn(5),
                'dataset2':np.random.randn(5)})

group1 = df['dataset1'].groupby(df['k1'])
group1
group1.mean()


cities = np.array(['NY','LA', 'LA','NY','NY'])
month = np.array(['JAN','FEB','JAV','FEB','JAN'])

# group the means by city
df['dataset1'].groupby([cities, month]).mean()

# pass columns names as group kesys
df.groupby('k1').mean()
# using multiple keys
df.groupby(['k1','k2']).mean()

#getting sizes
df.groupby(['k1']).size()

# iterate over groups
for name,group in df.groupby('k1'):
    print("This is the %s group" %name)
    print(group)
    print("\n")
    

for (k1,k2), group in df.groupby(['k1','k2']):
    print("key1 = %s Key2 %s" %(k1,k2))
    print(group)
    print("\n")
    

# create a dictionary
group_dict = dict(list(df.groupby('k1')))
# shows every row that has x
group_dict['X']

# setparation of types
group_dict_axis1 = dict(list(df.groupby(df.dtypes, axis=1)))

group_dict_axis1

# find the mean using both keys by grouping them
ds2_group = df.groupby(['k1','k2'])[['dataset2']]
ds2_group.mean()


"""
GroupBy on Dict and Series
"""

animals = DataFrame(np.arange(16).reshape(4,4), 
                    columns=['W','X','Y','Z'],
                    index=['Dog','Cat','Bird','Mouse'])
# adding nan values
animals.loc[1:2, ['W','Y']] = np.nan

behavior_map = {'W':'good','X':'bad','Y':'good','Z':'bad'}
animal_col = animals.groupby(behavior_map,axis=1)
animal_col.sum()


behave_series = Series(behavior_map)
animals.groupby(behave_series, axis=1).count()
#groups by sum of length name in index
animals.groupby(len).sum()

#use kesy as sub index
keys = ['A','B','A','B']
animals.groupby([len,keys]).max()
# multi index top use hierarchical arrays
hier_col = pd.MultiIndex.from_arrays([['NY','NY','NY','SF','SF'],[1,2,3,1,2]],
                                     names=['City','sub_values'])

df_hr = DataFrame(np.arange(25).reshape(5,5), columns=hier_col)
df_hr = df_hr* 100
df_hr

"""
Aggregation
Are operations that result in a scalar which you can add as a column to the data
as my own aggregation. 
"""
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'

dframe_wine = pd.read_csv('winequality-red.csv', sep=';')

dframe_wine.head()

# average alcohol content for the wine in percent
dframe_wine['alcohol'].mean()

# Own data aggregation
def max_to_min(arr):
    return arr.max() - arr.min()

#groupby
wino = dframe_wine.groupby('quality')
# group by quality
wino.describe()

#takes max of each column and subtracts the min
wino.agg(max_to_min)

wino.agg('mean')

# quality to alcohol content ratio
# add a new column to dataframe
dframe_wine['qual/alc ratio'] = dframe_wine['quality'] / dframe_wine['alcohol']
dframe_wine.head()

# pivot table
dframe_wine.pivot_table(index=['quality'])

# plotting alcohol vs quality scatter plot.
dframe_wine.plot(kind='scatter', x='quality', y='alcohol')


"""
Splitting Applying and combining 
"""
dframe_wine = pd.read_csv('winequality-red.csv', sep=';')
dframe_wine.head()

# highest alcohol content wine for each quality range
def ranker(df):
    df['alc_content_rank'] = np.arange(len(df)) + 1
    return df

dframe_wine.sort_values('alcohol', ascending=False, inplace=True)
dframe_wine = dframe_wine.groupby('quality').apply(ranker)
dframe_wine.head()


# finding the highest alcohol content for each rank
num_of_quality = dframe_wine['quality'].value_counts()
num_of_quality


dframe_wine[dframe_wine.alc_content_rank == 1].head(len(num_of_quality))


"""
Cross Tabulation
"""





















