# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy

# Importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values  # is a list of all the values in the table called 
                                 # features (x is a matrix)
y = dataset.iloc[:, 3].values    # is a list of the last column (y is a vector)

# Taking care of missing data and using the mean strategy
from sklearn.impute import SimpleImputer as Imputer
# From keras.utils import to_categorical

imputer = Imputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# encoding categorical data into values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_x = LabelEncoder()
label_encoder_x.fit_transform(x[:, 0])

# Changes the country names to values
x[:, 0] = label_encoder_x.fit_transform(x[:, 0])
onehutencoder = OneHotEncoder(categorical_features=[0])
x = onehutencoder.fit_transform(x).toarray()

# label encoder
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)

# Split data set into two sets, training and test set
# Training set is used to build the model and test set is used to test the 
# performance of the model from the training set. The results should not be 
# that much different

from sklearn.model_selection import train_test_split
# dependant and independant variable, 20% goes to test_set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# feature scalling variables need to be in the same scale

# Method 1
# X_standard = (x - mean(x)) / stdv(x)
# Method 2
# x_norm (x - min(x)) / (max(x) - min(x))

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
# Scalling dummy variables
# it depends on how much we want to keep interpretation in models
# it wont break model if i dont scale
