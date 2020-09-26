# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
# is a list of all the values in the table called
# x features (x is a matrix)
# y labels is a list of the last column (y is a vector) 
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values

# When data is very small there is no need to split the data.
# We have 10 elements in this training set
# Split data set into two sets, training and test set
# dependant and independant variable, 20% goes to test_set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# No need for feature scalling either
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
# Now create the squared matrix
# poly reg created the np.ones in the first column of matrix of features and 
# transormed matrix of features to x_poly
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly, y)
# We need to include the fit into a multiple linear regression model
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)


# Visualising the Linear Regression results
plt.scatter(x, y, color="red")
# ploting the real points and the predictions using lin_reg
# this model is not very good because it does not fit the points very well
plt.plot(x, lin_reg.predict(x), color="blue")
plt.title("Truth or Bluff (Linear Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()  # to display the graph

# Visualising the Polynomial Regression results
# min(x) lower value of x max(x) max value of x
# This gives uas a vector but we beed a matrix
x_grid = np.arange(min(x), max(x), 0.1)  # have a more advanced plot 
# Use reshape from numpy to change the vector to a matrix
x_grid = x_grid.reshape(len(x_grid), 1)  # number of lines/rows is number of elements 
                                         # of x_grid, and 1 columns
# plot x_grid instread of x
# this final graph is te continues line to polynomial                                        
plt.scatter(x, y, color='red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
# Visualising the Polynomial Regression results (for higher resolution and smoother 
# curve) The Polynomial Regression model is a much better fit for the type of data

# Predicting a new result with Linear Regression
lin_reg.predict([[6.5]])
# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))

# Evaluating the Model Performance
from sklearn.metrics import r2_score
r2_score(y, lin_reg_2.predict(poly_reg.fit_transform(x)))
