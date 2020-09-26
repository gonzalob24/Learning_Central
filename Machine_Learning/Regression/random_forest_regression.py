# Random Forest Regression

# Importing the dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting the Random Forest Regression to dataset using fit method
from sklearn.ensemble import RandomForestRegressor
# Changed the trees from 10 to 100
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(x, y)


# Predicting a new result
y_pred = regressor.predict([[6.5]])


# Evaluating the Model Performance
from sklearn.metrics import r2_score
r2_score(y, y_pred)


# Visualizing the Random Forest Regression
# Since this is also a non continuous model I will use 
# a higher resolution to show the discontinuities
# By changing 0.1 to 0.01 we get more intervals meaning more steps
# 10 votes were made to get each step, calculating many different averages
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color="red")
plt.plot(x_grid, regressor.predict(x_grid), color="blue")
plt.title("Truth or Bluss (Random Forest Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")











