
import seaborn as sns
import numpy as np
import pandas as pd
from numpy.random import randn
# stats
from scipy import stats

#plotting
import matplotlib as mpl
import matplotlib.pyplot as plt

dataset1 = randn(100)

plt.hist(dataset1)

dataset2 = randn(80)

plt.hist(dataset2, color='indianred')

# alpha is the transparensy level
# normalize the data when there are different number of 
plt.hist(dataset1, normed=True, color='indianred', alpha=0.5, bins=20)
plt.hist(dataset2, normed=True, alpha=0.5, bins=20)

data1 = randn(1000)
data2 = randn(1000)

sns.jointplot(data1, data2)

sns.jointplot(data1, data2, kind='hex')