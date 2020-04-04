import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


from pandas import Series, DataFrame
from sklearn.datasets import load_boston

# Getting and setting up the data.
boston = load_boston()

# understand what the data looks like
print(boston.DESCR)

# histogram of the number of houses.
plt.hist(boston.target, bins=50)
plt.xlabel('Prices in $1000s')
plt.ylabel('Number of houses')

# scatter plot 1 feature vs the target
# as the number of rooms increases so does the price
plt.scatter(boston.data[:,5], boston.target)
plt.ylabel('Price in $1000s')
plt.xlabel('Number of rooms')

# get only the data from boston df
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df.head()

boston_df['Price'] = boston.target
boston_df.head()

# Linear regresson plot using sns
sns.lmplot('RM', 'Price', data=boston_df)

# view image from a link
from IPython.display import Image
url = 'http://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Linear_least_squares_example2.svg/220px-Linear_least_squares_example2.svg.png'
Image(url)


# y=mx+b
# y=Ap
# A=[x 1]
# p=[m]
#   [b]
 
 
# set up X as edian room values
X = boston_df.RM

# or set up as DataFrame and add ones column

# Use vstack to make X two-dimensional
X = np.vstack([X, np.ones(len(X))]).T

# Set up Y as the target price of the houses.
Y = boston_df.Price

# Create the X array in the form [X 1]
X = np.array( [ [value, 1] for value in X ] )

# Now get out m and b values for our best fit line
m, b = np.linalg.lstsq(X, Y, rcond=None)[0]
# Create scatter plot
plt.plot(boston_df.RM, boston_df.Price, 'o')

# plot best fit line
x = boston_df.RM
plt.plot(x, m*x + b, 'r', label='Best Fit Line')






