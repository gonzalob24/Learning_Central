
"""
Logistic Regression used for classification of a dataset
Ex; spam or not spam, true false, 1 or 0. 

Only two possible outputs for now.


"""
# Data imports 
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Math
import math

# Dataset imports
import statsmodels.api as sm

# Plotting imports
import matplotlob.pyplot as plt
import seaborn as sns
sns.set_style('whitegrif')

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Evaluating ML results
from sklearn import metrics

def logistic(t):
    return 1.0 / (1 + math.exp((-1.0)*t))

# set t from -6 to 6 using 500 elements, linearly spaced
t = np.linspace(-6,6,500)
y = np.empty((len(t)))
count=0
for ele in t:
    y[count] = logistic(ele)
    count+=1

# plot
plt.plot(t, y)
plt.title('Logistic Function')