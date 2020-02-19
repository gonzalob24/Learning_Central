# Decision Tree Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv("Position_Salaries.csv")
# Features of matrix x
x = dataset.iloc[:, 1:2].values
# Dependent variable
y = dataset.iloc[:,2].values

# Fitting the Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
# use the default setting means square error
regressor = DecisionTreeRegressor(random_state = 0)
# Fit the regressor
regressor.fit(x, y)

# Predicting a new result
# Salary is slightly below
y_pred = regressor.predict([[6.5]])

# Visualizing the results
# This visualization plots the 10 observaitons and 
# Joins the data points with a stright line
# without any predictions useing the average
# Use the higher resolution to plot the results because 
# Its a non continuous model
plt.scatter(x, y, color = "red")
plt.plot(x, regressor.predict(x), color = "blue")
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()


# Visualizing the results for higher resolution and smoother curve
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = "red")
plt.plot(x_grid, regressor.predict(x_grid), color="blue")
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()


