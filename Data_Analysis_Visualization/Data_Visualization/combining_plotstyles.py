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