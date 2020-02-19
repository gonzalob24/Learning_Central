# SVR

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values  # is a list of all the values in the table called 
                                 # features (x is a matrix)
y = dataset.iloc[:, 2].values    # is a list of the last column (y is a vector)

# When data is very small there is no need to split the data.
# We have 10 elements in thsi training set

# Split data set into two sets, training and test set
"""
from sklearn.model_selection import train_test_split
# dependant and independant variable, 20% goes to test_set
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=0)
"""

# No need for feature scalling either becuase most classes do this already
# Feature Scaling SVR does not apply feature scalling in algo
# b/c SVR is not very common
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
# Fitting to the marix and scalling x and y
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y.reshape(-1, 1))

# Fitting SVR to the dataset. The 3 lines below create the SVR regressor
# rkb makes the kernel non linear
# For the last data point since it is very far from the other employees
# The SVR model decided to treat it as an outlier
from sklearn.svm import SVR
regressor = SVR(kernel= 'rbf')
regressor.fit(x, y)

# Predicting a new resukt with SVR
# This will give us the scalled version so we need to inverse with
# inverse_tranform method
y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))

# Visualising the SVR results                                       
plt.scatter(x, y, color='red')
plt.plot(x, regressor.predict(x), color='blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()



# Visualising the SVR results (for higher resolution and smoother curve)
x_grid = np.arange(min(x), max(x), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
