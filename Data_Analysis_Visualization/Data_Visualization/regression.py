#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:29:06 2020

@author: gonzalobetancourt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

from numpy.random import randn
from scipy import stats

tips = sns.load_dataset('tips')
tips.head()

#  tips vs ttotal bill
sns.lmplot('total_bill', 'tip', tips)

## I can specify the order of the polinomial
sns.lmplot('total_bill', 'tip', tips, order=4, 
           scatter_kws={'marker':'.', 'color':'indianred'},
           line_kws={'linewidth':1, 'color':'blue'})

# no regresion line
sns.lmplot('total_bill', 'tip', tips, fit_reg=False)

tips['tip_pect'] = 100 * (tips['tip']/tips['total_bill'])
tips.head()

# plot discrete variables
sns.lmplot('size', 'tip_pect', tips)

# look into what jitter is
sns.lmplot('size', 'tip_pect', tips, x_jitter=0.1)

sns.lmplot('size', 'tip_pect', tips, x_estimator=np.mean)