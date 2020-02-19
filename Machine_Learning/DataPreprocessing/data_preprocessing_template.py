# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values  # is a list of all the values in the table
y = dataset.iloc[:, 3].values  # is a list of the last column
print(x)
# Split data set into two sets, training and test set
# dependant and independant variable, 20% goes to test_set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# feature scalling variables need to be in the same scale
# Method 1
# X_standard = (x - mean(x)) / stdv(x)
# Method 2
# x_norm (x - min(x)) / (max(x) - min(x))
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
"""
