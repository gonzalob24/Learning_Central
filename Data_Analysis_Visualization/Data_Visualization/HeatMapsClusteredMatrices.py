#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:00:05 2020

@author: gonzalobetancourt
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy import stats

flights_df = sns.load_dataset('flights')
flights_df.head()

# pivot DF
flights_df = flights_df.pivot('month', 'year', 'passengers',)
flights_df.head()

sns.heatmap(flights_df)

sns.heatmap(flights_df, annot=True, fmt='d')

sns.heatmap(flights_df, center=flights_df.loc['January', 1955])

f,(axis1, axis2) = plt.subplots(2,1)

yearly_flights = flights_df.sum()
years = pd.Series(yearly_flights.index.values)
years = pd.DataFrame(years)

flights = pd.Series(yearly_flights.values)
flights = pd.DataFrame(flights)

year_df = pd.concat((years, flights), axis=1)
year_df.columns = ['Year', 'Flights']

sns.barplot('Year', y='Flights', data=year_df, ax=axis1)
sns.heatmap(flights_df, cmap="Blues", ax=axis2, cbar_kws={'orientation':'horizontal'})

sns.clustermap(flights_df)


sns.clustermap(flights_df, col_cluster=False)

# standard scale
# scale the cols
sns.clustermap(flights_df, standard_scale=1)
# Scale the rows
sns.clustermap(flights_df, standard_scale=0)

# Scale with z-score
sns.clustermap(flights_df, z_score=1)







