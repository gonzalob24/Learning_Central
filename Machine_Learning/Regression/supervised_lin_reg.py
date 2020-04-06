import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
sns.set_style('whitegrid')


from pandas import Series, DataFrame
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Getting and setting up the data.
boston = load_boston()

# understand what the data looks like
print(boston.DESCR)

# histogram of the number of houses.
plt.hist(boston.target, bins=50)
plt.xlabel('Prices in $1000s')
plt.ylabel('Number of houses')

# scatter plot, 1 feature vs the target
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

# Linear regresson plot using lmplot
sns.lmplot('RM', 'Price', data=boston_df)

# view image from a link: LSM image of what I am trying to do
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

# Use vstack to make X two-dimensional however it is not needed in this case
# X = np.vstack(X)
# X = np.vstack([X, np.ones(len(X))]).T

# Set up Y as the target price of the houses.
Y = boston_df.Price

# Create the X array in the form [X 1]
X = np.array( [ [value, 1] for value in X ] )

# Now get out m and b values for our best fit line
m, b = np.linalg.lstsq(X, Y, rcond=None)[0]

# Create scatter plot
plt.plot(boston_df.RM, boston_df.Price, 'o')
# plot the best fit line
x = boston_df.RM
plt.plot(x, m*x + b, 'r', label='Best Fit Line')


# Finding the error in the best fit line
result = np.linalg.lstsq(X, Y)

# Get the total error,m stored at index 1
error_total = result[1]

# Get the root mean square error
rmse = np.sqrt(error_total/len(x))

# RMSE corresponds to approximately the standard deviation. I can say that 
# the proce of a house won't vary more than 2 times the RMSE 95% of the time.
print('The root mean squared error was {:.2}'.format(rmse[0]))

# Create a LinearRegression Object
# use the .fit() to fit the linerar model 
# use .predict() for prediction
# use .score() which returns the coefficients of determinators (R^2)
lreg = LinearRegression()

# Data columns
X_multi = boston_df.drop('Price', axis=1)

# Targets
Y_target = boston_df.Price

# Fit the data to the lreg model
lreg.fit(X_multi, Y_target)


print('The estimated intercept coefficient is {:.2f}'.format(lreg.intercept_))
print("The number of coefficients used {}".format(len(lreg.coef_)))

# set a DF for the features
coeff_df = DataFrame(boston_df.columns)
coeff_df.columns = ['Features']

# Set a new column lining up the coefficients from the linear regression
coeff_df['Coefficients Estimate'] = pd.Series(lreg.coef_)


############## Using training and validation sets ##################

# Grab the output and set X and Y test and train data sets
X_train, X_test, Y_train, Y_test = train_test_split(X, boston_df.Price, test_size=0.2)

# Predicting prices

# creat the linear regression
lreg = LinearRegression()
# fit the training set
lreg.fit(X_train, Y_train)

# predictions
pred_train = lreg.predict(X_train)
pred_test = lreg.predict(X_test)

print('Fit a model with x train and calculate the MSE with y train: {:.2f}'.format(np.mean((Y_train-pred_train)**2)))
print('Fit a model with x train and calculate the MSE with x and y test: {:.2f}'.format(np.mean((Y_test-pred_test)**2)))


# Scatter plot the training test to visualize the errors
train = plt.scatter(pred_train, (Y_train-pred_train), c='b', alpha=0.5)


# scatter pltit he testing data
test = plt.scatter(pred_test, (Y_test-pred_test), c='r', alpha=0.5)

plt.hlines(y=0, xmin=-10, xmax=10)
plt.legend((train, test), ('Trainin', 'Test'), loc='lower left')
plt.title('Residual Plot')


# sns residual plot 
sns.residplot('RM', 'Price', data=boston_df)