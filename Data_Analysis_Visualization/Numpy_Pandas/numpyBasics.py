# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import os

# arrays and matrix based
my_list1 = [1,2,3,4]

my_array1 = np.array(my_list1)

my_list2 = [11, 22, 33, 44]

my_lists = [my_list1, my_list2]

my_array2 = np.array(my_lists)

my_array2.shape # 2 x 4 array

my_array2.dtype  # check the type

my_zeros_array = np.zeros(5)  # array of 5 zeros
my_zeros_array.dtype

my_ones_array = np.ones([5, 5])  # 5 x 5 array of 1's
my_ones_array2 = np.ones((5,5))

np.empty(5)  # create an empty array

identity_matrix = np.eye(5)  # identity matrix
identity_matrix2 = np.identity(5)

array_arange = np.arange(5, 50, 2)  # similar to range()


# Using arrays and scalars
arr1 = np.array([[1,2,3,4], [8, 9, 10, 11]])

# multiply arrays
arr1 * arr1

# Subtraction
arr1-arr1

1 / arr1

arr1**3

"""
Indexing Arrays
"""

arr = np.arange(0, 11)
arr[8]

arr[1:5]  # prints 1 just before 5

# setting a value with index
arr[0:5] = 100

arr = np.arange(0, 11)

# slicing an array just like in python
slice_of_arr = arr[0:6]

slice_of_arr[:] = 99  # this will affect original array due to objects pointing to same location

arr_copy = arr.copy()  # this makes a copy of arr and changes to the copy wont affect arr

arr_copy[0:5] = 22

arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
arr_2d[1]  # first row
arr_2d[1][0]

arr_2d[:2, 1:]

# Fancy indexing
arr2d = np.zeros((10, 10))
arr_length = arr2d.shape[1]

for i in range(arr_length):
    arr2d[i] = i

arr2d[[2, 4, 6, 8]]

"""
Transposition
"""

arr = np.arange(50).reshape((10, 5))

# transpose
arr_t = arr.T
# dot product
np.dot(arr_t, arr)

arr3d = np.arange(50).reshape((5,5,2))
arr3d_t = arr3d.transpose((1,0,2))

arr = np.array([[1,2,3]])

arr = arr.swapaxes(0,1) # changing the orientation 

"""
Universal array functions
"""

arr = np.arange(11)
np.sqrt(arr)
np.exp(arr)

# Creating a random array with normal distribution
A = np.random.randn(10)
B = np.random.randn(10)

# Binary functions
np.add(A, B)
np.maximum(A, B)
np.minimum(A, B)

website = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'
import webbrowser
webbrowser.open(website)

"""
Array Processing
"""
# creating a grid
points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)

z = (np.sin(dx) + np.sin(dy))  # sine of all dx + sine of all dy values


# plotting
plt.imshow(z)
plt.colorbar()
plt.title("Plot for sin(x) + sin(y)")

# numpy where
A = np.array([1,2,3,4])
B = np.array([100, 200, 300, 400])
 
# boolean array
condition = np.array([True, True, False, False])

# use the boolean array for list comprehension
answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A,B,condition)]
answer2 = np.where(condition, A, B)
arr = randn(5,5)
np.where(arr<0, 0, arr)  # condition, replace, leave alone

arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr2.sum()
arr2.sum(axis=0) # add all columns

arr2.mean()
arr2.std()
arr2.var()

# Boolean array
bool_arr = np.array([True, False, True])
bool_arr.any()  # If anything is True return True
bool_arr.all()  # Are they all True

# Sort

arr = randn(5)
arr.sort()
arr

countries = np.array(['France', 'Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])
np.unique(countries)  # which ones only appeared once
# Checks to see of these countries are in countries array
np.in1d(['France', 'USA', 'Sweden'], countries) 

"""
Array Input Output
"""
arr = np.arange(5)

np.save('myarray', arr)
np.load('myarray.npy')

arr1 = np.load('myarray.npy')
arr2 = np.arange(10)
np.savez('ziparray.npz', x=arr, y=arr2)
array_archives = np.load('ziparray.npz')
array_archives['x']
array_archives['y']


arr3 = np.array([[1,2,3], [4,5,6]])

np.savetxt('mytextarray.txt',arr3, delimiter=',')
arr4 = np.loadtxt('mytextarray.txt', delimiter=',')




"""
---------------------------------------------------------------------
problems
"""

arr = np.arange(9)
arr2 = np.array([1,2,3,4])

# test if no elements are zerp
np.all(arr)

#checks if none are zero
np.any(arr2)

# test if no elements are nan or infinte
arr3 = np.array([1,2,np.nan, np.inf])
np.isnan(arr4)
np.isfinite(arr3)
np.isinf(arr3)
np.isnan(arr3)

# test for positive or negative infinity
arr4 = np.array([1,2,3,np.negative(np.inf)])
np.isneginf(arr4)

# test for complex, real, and is given number a scalar
arr5 = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

np.iscomplex(arr5)
np.isreal(arr5)
np.isscalar(3.1)
np.isscalar([3.1])


# test if two arrays are equal within a tolerance
np.allclose([1e10, 1e-7], [1.00001e10, 1e-8])
np.allclose([1e10,1e-8], [1.00001e10,1e-9])
np.allclose([1.0, np.nan], [1.0, np.nan])
np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)


# comparing >, <, >=, <=
arr7 = np.array([1,2,3,4])
arr8 = np.array([4,2,5,1])
arr7 < arr8
arr7 > arr8
arr7 <= arr8
arr7 >= arr8

# OR
np.less(arr7, arr8)
np.greater(arr7, arr8)
np.less_equal(arr7, arr8)
np.greater_equal(arr7, arr8)

# Size of memory occupied
arr9 = np.array([1,7,13,105])
arr9.size * arr9.itemsize


# create an array of 10 zeros, ones, fives
arr10 = np.zeros(10)
arr11 = np.ones(10)
arr12 = np.array([5]*10)
arr13 = np.ones(10)*5

# Integers from 30 to 70
arr14 = np.arange(30, 71, 1)

# Integeers form 30 to 70 only evens
arr15 = np.arange(30, 71, 2)

# 3x3 identity matrix
arr16 = np.identity(3)

# random numbers between 0 and 1
random_num_0_1 = np.random.normal(0,1,1)

# array with 15 random numbers
arr17 = np.random.normal(0,1,15)

#create a vector with values 15-55 and print all except first and last
vector = np.arange(15,55)
vector[1:-1]


# create a 3x4 array
array18 = np.arange(12).reshape((3,4))
# iterate over the array
for i in np.nditer(array18):
    print(i, end=" ")

# create vector of length 10 evenly distributed between 5 and 50
arr19 = np.linspace(5,49, 10)

# create vector values 0 to 20 and change the sign of the numbers in the range for 9 to 15
arr20 = np.arange(21)

arr20[(arr20 >= 9) & (arr20 <= 15)] *= -1

arr20[arr20==5] = -99

# create vector of length 5 filled with arbitrary numbers 0 to 10
arr21 = np.random.randint(0, 11, 5)

# multiply two vectors
arr22 = np.random.randint(0,11,5)

arr21 * arr22

# Create 3x4 matrix filled with values 10 to 21
mat1 = np.arange(10,22,1).reshape((3,4))

# find the number of rows and columns in a given matrix
mat1.shape

# create 10x10 matrix in which the border elements will be equal to 1 and inside 0
mat2 = np.ones((10,10))
# select all except first row and last row, first col and last col
mat2[0:-1, 1:-1] = 0

# create 5x5 zero matrix
mat3 = np.zeros((5,5))
mat3 = np.diag(np.arange(1,6,1))

# create 4x4 matrix in which 0 and 1 are staggered with zeros on the main diagnal
mat4 = np.zeros((4,4))
mat4[::2, 1::2] = 1
mat4[1::2, ::2] = 1

mat5 = np.random.randn(27).reshape((3,3,3))
# getting the sum of the array
mat5.sum()

#getting the sum of columns or rows
# sum of columns
mat5.sum(axis=0)
#sum of the rows
mat5.sum(axis=1)

# inner product is the dot product of two vectors.
 
# add a vector to each row of a matrix
arr = np.array([1,2,3])
mat6 = np.arange(12).reshape((4,3))
# create empty matrix to store values
results = np.empty_like(mat6)
for i in range(4):
    results[i, :] = mat6[i, :] + arr

# savoing a file
arr_saved = np.arange(20).reshape((4,5))
np.save('arr_saved',arr_saved)
# check if file exists
if os.path.exists('arr_saved.npy'):
    loaded_file = np.load('arr_saved.npy')
    print(np.array_equal(arr_saved, loaded_file))

# save two files ina single file compressed and then load it
arr1 = np.arange(5)
arr2 = np.arange(7)
np.savez('two_arrays', x=arr1,y=arr2)
loaded_arrs = np.load('two_arrays.npz')
loaded_arrs['x']
loaded_arrs['y']

# Save to a text file
array_text = np.arange(12).reshape((4,3))
header = 'col1 col2 col3'
np.savetxt('array_text.txt', array_text, fmt='%d', header=header)
loaded_txt = np.loadtxt('array_text.txt')
print(loaded_txt)

# plotting points
x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x)

plt.plot(x, y)
plt.title('Plott of sin(x)')
plt.ylabel('sin(x)')
plt.xlabel('x values')
plt.show()

arr = np.arange(2,10)
zero_vector = np.zeros(10)
zero_vector[6] = 11

#convert int array to float
arr_float = np.asfarray(arr)

# make matrix of ones and in the middle change the values to zeros
mat_ones = np.ones(25).reshape((5,5))
x = np.pad(mat_ones, pad_width=1, mode='constant', constant_values=0)

mat_8_8 = np.zeros(64).reshape((8,8))
mat_8_8[::2, ::2] = 1
mat_8_8[1::2, 1::2] = 1


