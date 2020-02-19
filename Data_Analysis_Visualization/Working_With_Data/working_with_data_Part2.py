# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

import sys
import json

#@ merging datasets
dframe1 = DataFrame({'key':['X','Z','Y','Z','X', 'X'],'data_set_1':np.arange(6)})

dframe2 = DataFrame({'key':['Q', 'Y', 'Z'], 'data_set_2':[1,2,3]})

# merges the common ones and automatically ovelaps where the keys matched 
pd.merge(dframe1, dframe2)

# choose whicjh colum to merge
pd.merge(dframe1, dframe2, on='key')

# which data keys to use
pd.merge(dframe1, dframe2, on='key', how='left')
pd.merge(dframe1, dframe2, on='key', how='right')

# many to many merge
dframe3 = DataFrame({'key':['X','X','X','y','Z','Z'], 'data_set_3': range(6)})
dframe4 = DataFrame({'key':['Y','Y','X','X','Z'], 'data_set_4': range(5)})
pd.merge(dframe3, dframe4)

# merge with multiple keys
df_left = DataFrame({'key1':['SF','SF','LA',], 
                     'key2':['one','two','one'], 
                     'left_data':[10,20,30]})

# outer merges the union
df_right = DataFrame({'key1':['SF','SF','LA', 'LA'], 
                      'key2':['one','one','one','two'],
                      'right_data':[40,50,60,70]})

pd.merge(df_left, df_right, on=['key1','key2'], how='outer')

# what does left data have for LA one 30.0

pd.merge(df_left, df_right, on='key1')


pd.merge(df_left, df_right, on='key1', suffixes=('_lefty','_righty'))



"""
Merge on index
"""

df_left = DataFrame({'key':['X','Y','Z','X','Y'],
                     'data':range(5)})

df_right = DataFrame({'group_data':[10,20]}, index=['X','Y'])

# Merge using the key for left df and index for the right df
pd.merge(df_left, df_right, left_on='key', right_index=True)

# using a hierarchy when merging
df_left_hr = DataFrame({'key1':['SF','SF','SF','LA','LA'],
                        'key2':[10,20,20,30,30],
                        'data_set':np.arange(5)})

df_right_hr = DataFrame(np.arange(10).reshape((5,2)), index=[['LA', 'LA', 'SF','SF','SF'],
                        [20,10,10,10,20]], columns=['col_1', 'col_2'])


# merge left by using keys and right with index
pd.merge(df_left_hr, df_right_hr, left_on=['key1','key2'], right_index=True)

df_left.join(df_right)


"""
Concatenate
Joing dataframes and matrices 
"""

arr1 = np.arange(9).reshape(3,3)
np.concatenate([arr1, arr1], axis=1)

np.concatenate([arr1, arr1], axis=0)

# concatenate in Pandas
ser1 = Series([0,1,2], index=['T','U','V'])
ser2 = Series([3,4], index=['X','Y'])

pd.concat([ser1, ser2])

pd.concat([ser1, ser2], axis=1)

pd.concat([ser1, ser2], keys=['cat1','cat2'])

# in data frames
dframe1 = DataFrame(np.random.randn(4,3), columns=['X','Y','Z'])
dframe2 = DataFrame(np.random.randn(3,3), columns=['Y','Q','X'])

pd.concat([dframe1, dframe2])

pd.concat([dframe1, dframe2], ignore_index=True)


"""
Combine DataFrames
"""

ser1 = Series([2, np.nan, 4, np.nan, 6, np.nan], index=['Q','R','S','T','U','V'])
ser2 = Series(np.arange(len(ser1)), dtype=np.float64, index=['Q','R','S','T','U','V'])

# where ser1 is null select ser2 value if not put in ser1 value
Series(np.where(pd.isnull(ser1), ser2, ser1), index=['Q','R','S','T','U','V'])
# this does the same as above
ser1.combine_first(ser2) ################ faster code

# in dataframes
nan = np.nan
df_odds = DataFrame({'X':[1.,nan,3.,nan], 'Y':[nan, 5., nan, 7.], 'Z':[nan, 9., nan, 11.]})
df_evens = DataFrame({'X':[2., 4., nan,6., 8.], 'Y':[nan, 10., 12., 14., 16.]})

df_odds.combine_first(df_evens)


"""
Reshaping
"""
df = DataFrame(np.arange(8).reshape(2,4),
               index=pd.Index(['LA','SF'], name='city'),
               columns=pd.Index(['A','B','C','D'], name='letter'))


# use stack to swap index and colums 
df_st = df.stack()

df_st.unstack()

df_st.unstack('letter')
df_st.unstack('city')

ser1 = Series([0,1,2], index=['Q','X','Y'])
ser2 = Series([2,4,6], index=['X','Y','Z'])

df1 = pd.concat([ser1, ser2], keys=['Alpa','Beta'])

# turn in to dataframe with unstack
df1.unstack()

# filter out nan values
df1.unstack().stack()


df1 = df1.unstack()

# keep the nan values when stacking an unstack
df1.stack(dropna=False)


"""
Pivot Tables
1. What am I seeking? What info do I want to know?
"""

# pandas testing utility
# Lets create some data to play with:

# Note: It is not necessary to understand how this dataset was made to understand this Lecture.

#import pandas testing utility
import pandas.util.testing as tm 

tm.N = 3

#Create a unpivoted function
def unpivot(frame):
    N, K = frame.shape
    
    data = {'value' : frame.values.ravel('F'),
            'variable' : np.asarray(frame.columns).repeat(N),
            'date' : np.tile(np.asarray(frame.index), K)}
    
    # Return the DataFrame
    return DataFrame(data, columns=['date', 'variable', 'value'])

#Set the DataFrame we'll be using
dframe = unpivot(tm.makeTimeDataFrame())

# know that variables for particular dates -- row col value
dframe_piv = dframe.pivot('date','variable','value')


"""
Finding Duplciate values in Dataframe
"""

dframe = DataFrame({'key1':['A']*2 + ['B']*3,
                    'key':[2,2,2,3,3]})

# finding duplicates
dframe.duplicated()

# dop duplicates
dframe.drop_duplicates()


# select the duplicates to drop in this example from key1
dframe.drop_duplicates(['key1'])

dframe.drop_duplicates(['key1'], keep="last")


"""
Mapping
"""

# Mapping is a greate way to add columns to dataframes

dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],
                    'altitude':[3158,3000,2762]})


# add a colum to each state tje city is in
state_map = {'Alma':'Colorado','Brian Head':'Utah','Fox Park':'Wyoming'}
# create a new column called state calling the map method onto the city column
dframe['state'] = dframe['city'].map(state_map)

"""
Replace
"""

ser1 = Series([1,2,3,4,1,2,3,4])

# using replace when can select which value I want to replace
# replace, with
ser1.replace(1, np.nan)
# lists can also be passed
ser1.replace([1,4], [100,400])

# can also pass a dictionary
ser1.replace({4:np.nan})

dframe.replace({'Alma':'SEA'})



"""
Rename
"""
dframe = DataFrame(np.arange(12).reshape(3,4),
                   index=['NY','LA','SF'],
                   columns=['A','B','C','D'])
dframe.index.map(str.lower)
# makes the index lower case
dframe.index = dframe.index.map(str.lower)

# rename
dframe.rename(index=str.title, columns=str.lower)

# passing dictionaries for index and columns to rename them
dframe.rename(index={'ny':'New York'}, 
              columns={'A':'Alpha'})

# inplace edits the dataframe in place
dframe.rename(index={'ny':'New York'}, 
              columns={'A':'Alpha'}, inplace=True)


"""
Binning
"""

years = [1990, 1991, 1992, 2008, 2012, 2015, 1987, 1969, 2013, 2008, 1999]

decade_bins = [1960, 1970, 1980, 1990, 2000, 2010, 2020]

# category objects with cut
decade_category = pd.cut(years, decade_bins)
decade_category.categories

# value counts in each category
pd.value_counts(decade_category)

# pass data values to the cut
pd.cut(years, 2, precision=1)


"""
Outliers
"""

np.random.seed(12345)
# 1000 rows and 4 columns
dframe = DataFrame(np.random.randn(1000,4))
dframe.head()

stats_dframe = dframe.describe()

col = dframe[0]
col.head()

# which values in col are greater than 3
col[np.abs(col) > 3]
# in any column
dframe[(np.abs(dframe) > 3).any(1)]

# anywhere in dframe where abs() > 3 set that equal to sign of that value
# and multiply it by 3
# used to cap liers
dframe[np.abs(dframe) > 3] = np.sign(dframe) * 3
dframe.describe()


"""
Permutations
"""
# randomly reorder in a series or dataframe

df = DataFrame(np.arange(16).reshape(4,4))
# created a random permutation
blender = np.random.permutation(4)

# get a permutation of the rows
df.take(blender)

# box with 3 marbles
box = np.array([1,2,3])
# permutaiton with replacement, size is how many times to pick from the box
shaker = np.random.randint(0, len(box), size= 10)

# simulates taking a marble with replacement
hand_grabs = box.take(shaker)


















































































































