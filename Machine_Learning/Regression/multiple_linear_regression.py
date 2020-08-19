# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset --> which start up to invest in
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# encoding categorical data into values
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# label_encoder_x = LabelEncoder()
# x[:, 3] = label_encoder_x.fit_transform(x[:, 3])

# Changes the country names to values
# onehutencoder = OneHotEncoder(categories=[3], sparse=False)
# x[:,3] = onehutencoder.fit_transform(x[:,3].reshape(-1,1)).toarray()
# Encode independent variables into values using onehot encoding with sklearn
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x)) # returns new matrix      

# always omit one dummy variable
# Avoiding the dummy variable trap
# the linear model will remove it form me b/c it will select the 
# best parameters for the best fit line
# x = x[:, 1:]

# Split data set into two sets, training and test set
from sklearn.model_selection import train_test_split
# dependant and independant variable, 20% goes to test_set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""

# Fitting Muiltiple Linear Regression to the Trainin set
from sklearn.linear_model import LinearRegression
# regressor object
regressor = LinearRegression()
# FIt the regressor to training set
regressor.fit(x_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(x_test)
np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(-1,1), y_test.reshape(-1,1)),1))
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)), 1))


# Building the optimal model using Backward Elimination
# Remove non statistically important variables.
import statsmodels.api as sm
x = np.append(arr=np.ones((50, 1)).astype(int), values=x, axis=1)  # axis is either 0 or 1

# Optimal matrix of features, variables that have high impact on profits
# Remove the variables that are not statistically significant, one by one
x_opt = x[:, [0, 1, 2, 3, 4, 5]]
# 1. Select the SL to stay in the model SL = 0.05
# 2. Fit the full model with all possible predictors

# Create a new regressor
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary() # remove the PL above .95

# remove the second index as shown in previous summary()
x_opt = x[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary() # remove the PL above .95

x_opt = x[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary() # remove the PL above .95

x_opt = x[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary() # remove the PL above .95

x_opt = x[:, [0, 3]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary() # remove the PL above .95
