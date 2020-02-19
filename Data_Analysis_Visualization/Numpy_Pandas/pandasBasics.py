#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 00:45:43 2020

@author: gonzalobetancourt
"""

# Going over series, a series is like an array except that is has labels
import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame
import webbrowser

"""
                                    Series
                                -------------
One-dimensional labeled array or data structure for a single data frame

"""

obj = Series([3,6,9,12])

obj.values
obj.index

# Creating a series and specifing the index for each value
ww2_casualties = Series([87000000, 43000000,3000000, 21000000, 400000], index=['USSR','Germany','China','Japan','USA'])
ww2_casualties['USA']

# Useing operations with series
# Check which countries had casualties greater than 4mil
ww2_casualties[ww2_casualties > 4000000]

# we can also treat the series as an ordered dictionary
'USSR' in ww2_casualties

# Changing the series into a dictionary
ww2_dict = ww2_casualties.to_dict()

# Convert back to a series
ww2_series = Series(ww2_dict)

# list of countries 
# Since Argentina is not in ww2_dict it will have nan
countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
obj2 = Series(ww2_dict, index=countries)
obj3 = Series(ww2_casualties, index=countries)

# checks for null values in data
pd.isnull(obj2)

# check for items that are not null
pd.notnull(obj2)

# add objects to series to series and will align items by index
ww2_series + obj2

# Nameing object and the index
obj2.name = "WW2 Casualties"
obj2.index.name = "Countries"


"""
DataFrames
"""

websites = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(websites)

nfl_frame = pd.read_clipboard()
# get the column names
nfl_frame.columns

# Grab column name
#name.ColName
nfl_frame.Rank

# columns with multiple words
nfl_frame['First NFL Season']

# Grabbing multiple columns I create a new data frame
DataFrame(nfl_frame, columns=['Team', 'First NFL Season', 'Total Games'])

# Column that does not exist
DataFrame(nfl_frame, columns=['Team', 'First NFL Season', 'Total Games', 'Stadium'])

# Rows first 4
nfl_frame.head()
# last 4
nfl_frame.tail()


#using indes
nfl_frame.ix[3]


# assign values to entire columns
nfl_frame['Stadium'] = "Levi's Stadium"
nfl_frame['Stadium'] = np.arange(6)

# adding a series to a data frame
stadiums = Series(["Levi's Stadium", "AT&T Stadium"], index=[5, 0])
# input the above to the data frame
nfl_frame['Stadium'] = stadiums

# delete colums
del nfl_frame['Stadium']

# DataFrame can accept a dictionary
data = {'City':['SF','LA','NYC'], 'Population':[837000, 3880000, 8400000]}

city_frame = DataFrame(data)


"""
Index Objects
"""
my_ser = Series([1,2,3,4], index=['A','B','C','D'])
my_index = my_ser.index
my_index
# grabbing an index
my_index[2]

my_index[2:]
my_index[::-1]

my_index[0] 

# Indexes are immutable you can't change them, which makes the index more stable
# I can reindex 
my_index[0] = 'Z'


"""
Reindex
"""
ser1 = Series([1,2,3,4], index=['A','B','C','D'])

# rearange data to a new index
# Since E and F did not exist the values will be nan
ser2 = ser1.reindex(['A','B','C','D','E','F'])

# fill in values G gets filled with 0
ser2.reindex(['A','B','C','D','E','F','G'], fill_value=0)

# other methods to fill values
ser3 = Series(['USA','Mexico','Canada'], index=[0,5,10])

# reindex from 0-14 ser3
ranger = range(15)

#if methos was not there the index will be nan
ser3.reindex(ranger, method='ffill')  # forward fill grabs prev. value and forward fills it

# reindex rows or columns
dataframe = DataFrame(randn(25).reshape((5,5)), index=['A','B','D','E','F'], 
                      columns=['col1','col2','col3','col4','col5'])

# reindex since we forgot c
dataframe2 = dataframe.reindex(['A','B','C','D','E','F'])
new_columns = ['col1','col2','col3','col4','col5','col6']
dataframe2.reindex(columns=new_columns)

# use .ix to reindex
dataframe2.ix[['A','B','C','D','E','F'], new_columns]


"""
Drop Entry from Series and DataFrames
"""
ser1 = Series(np.arange(3), index=['a','b','c'])

# drop an index
ser1.drop('b')

dframe = DataFrame(np.arange(9).reshape((3,3)), index=['SF','LA','NY'], columns=['pop','size','year'])

# dropping a row
dframe.drop('LA')


#dropping a column
dframe.drop('year', axis=1)

# Selecting enrtries in the dataframe

series1 = Series(np.arange(3), index=['A','B','C'])
# Double the series
series1 = 2*series1

# Selecting data by index name, can use slicing
series1['B']
series1[1]
series1[0:3]
# Call them by a list of names
series1[['A','B']]

# use logic to access values
series1[series1 > 3]
# setting values using this method
series1[series1 > 3] = 10


# Now in a dataframe
dframe = DataFrame(np.arange(25).reshape((5,5)), index=['SF','DC','Chi','NYC','LA'], 
                   columns=['A','B','C','D','E'])

# Selecting data from data frame
dframe['B']
# Selecting 2 columns
dframe[['B','E']]
# using logic
dframe[dframe['C'] > 8]
# Returns boolean
dframe > 10
# using ix to return the rows.
dframe.ix['LA']
dframe.ix[1]



"""
Data Alignment
"""
series = Series([0,1,2], index=['A','B','C'])
series1 = Series(np.arange(3), index=['A','B','C'])

series2 = Series([3,4,5,6], index=['A','B','C','D'])

series + series2

# Now try this with dataframes
dframe = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'), index=['NYC','LA'])
dframe2 = DataFrame(np.arange(9).reshape((3,3)), columns=list('ADC'), index=['NYC','SF','LA',])
# when we add these two data frames only LA and NYC for A column, this is the only
# one that matches the other ones are nan values
dframe + dframe2

# What of we want to replace nan. Adding different size data frames and allows
# me to keep data
dframe.add(dframe2, fill_value=0)

# operations
ser3 = dframe2.iloc[0]
dframe2 - ser3


"""
Rank and Sort
"""

# not in order so that I can sort it
ser1 = Series(np.arange(3), index=['C','A','B'])

# sorts by index
ser1.sort_index()

# sort by value not index
ser1.sort_values()
ser2 = Series(randn(10))

# sort by value lowest to highes
ser2.sort_values()

# ranking the values
ser2.rank()
ser2.rank()

ser3 = Series(randn(10))
ser3 = ser3.rank()
ser3.sort_values()


"""
Series Problems
"""
# Create 1 d series
one_d = Series([3,2,1,4,5])
one_d2 = Series(np.arange(1,6,1))

# Convert series to list and type
type(one_d2)
one_d = one_d.to_list()
type(one_d)

# subtrract, add, multioly, divide same as numpy
# Equality operators is done the same way
one_d == one_d2
one_d > one_d2
one_d >= one_d2
one_d < one_d2
one_d <= one_d2

# convert dictionary, array, list to series

dictionary = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
dict2 = Series(dictionary)

# Change datatype of a given column in a series
arr = [100, 200, 'Python',  300.12, 400]
ser = Series(arr)
# errors = 'coerce' changes valeus nan if they are not numeric
ser_numeric = pd.to_numeric(ser, errors='coerce')

# Convert first column of daaframe into a series
dataframe1 = DataFrame(([1,2,3,4,7,11],[4,5,6,9,5,0],[7,5,8,12,1,11]), columns=['col1','col2','col3','col4','col5','col6'])

ser_from_df1 = dataframe1.iloc[:, 0:1]

# convert series to an array 
# NOTE: series does not have a to array method.
series10 = Series(['100', '200', 'python', '300.12', '400'])
series_to_array = np.array(series10.tolist())

"""
Keep this problem in mind
"""

# convert series of lists to one series
ser1 = Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
ser1_one = ser1.apply(Series).stack().reset_index(drop=True)

# Sort a series
arr = ['100', '200', 'Python',  '300.12', '400']
arr = Series(arr)
arr_sort = arr.sort_values()
new_arr = arr.append(Series(['500', 'php']))

# New subset of a series based on a given condition

ser2 = Series(np.arange(10))
ser2_condition = ser2[ser2 < 6]

# change the order of the index
ser3 = Series(np.arange(1,6,1), index=['A','B','C','D','E'])
ser3 = ser3.reindex(index=['B','A','C','D','E'])

#Get mean and std of series
ser_mean_sd = Series([1,2,3,4,5,6,7,8,9,5,3])
ser_mean_sd.mean()
ser_mean_sd.std()


# Get items in given series not present in another
ser1 = Series([1,2,3,4,5])
ser2 = Series([2,4,6,8,10])

new_ser = ser1[~ser1.isin(ser2)]

#Union of two series
ser_union = Series(np.union1d(ser1, ser2))

# Intersection of two series, values that are thes same
ser_intersection = Series(np.intersect1d(ser1, ser2))
not_common_in_both = ser_union[~ser_union.isin(ser_intersection)]
