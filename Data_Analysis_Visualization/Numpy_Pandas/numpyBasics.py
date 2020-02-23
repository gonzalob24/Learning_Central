# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy import misc
import sklearn.datasets
import scipy
import matplotlib.pyplot as plt
from numpy.random import randn
import os

# arrays and matrix based
my_list1 = [1,2,3,4]

my_array1 = np.array(my_list1, dtype = np.int32)
ones = np.ones((3,2), dtype = np.int32)
m1 = np.empty((3,2))

np.set_printoptions(threshold=np.nan)

eye = np.eye(4) # creates an identity matrix

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
arr_2d[0:-1, :]
arr_2d[0, ...] ## used to denote the rest of the array
arr_2d[0, :]
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
# iterations
arr_iter = np.arange(16).reshape(4,4)
arr_reshape = arr_iter.reshape(-2,8)

test = np.arange(1,201, 1).reshape(25,8)
test_ones = np.ones_like(test)
test[-20:, 2:6]

arr_flatt = arr_iter.flatten()
arr_flatt2 = arr_iter.ravel()

for i in np.nditer(arr_iter):
    print(i)

for i in np.nditer(arr_iter, order='F', flags=['external_loop']):
    print(i)

arr_square = arr_iter ** 2

for arr in np.nditer(arr_iter, op_flags=['readwrite']):
    arr[...] = arr * arr
    
# name.ravel() # applied to any object
# name.flatten() # belongs to any array object by numpy arrays
arr_iter.T  # transpose

# can also reshape the arra with .reshaope(r,c)
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
Advanced Operationa with Numpy Array
---------------------------------------------------------------------
"""
# Splitting numpy array
p = np.arange(12)

p_split = np.split(p, 4)
p_split2 = np.split(p, [3, 8]) # spltis at these indices

names = np.array([('IBM', 'apple', 'intel', 'sony', 'dell', 'akamai'),
                  ('NY', 'CA', 'CA', 'TX', 'WA', 'MASS')])

x1, x2 = np.hsplit(names, 2) # column wise
y1, y2 = np.vsplit(names, 2) # row wise

# Images are multidimensional arrays. Every pixel in an imgae cab be
# represented by a number. Each pizel is represented by RGB, 3 colors
# Each RGB is represented by a number 0-255

# grayscale: every pixel only represents the intensity information
# 0.0 -- > black 
# 1.0 --> white

# pixel --> 1 byte o data

# single chanel are grayscale (#, #, 1)
# multi-channel are colored images (#,#,3)
from skimage import io
import matplotlib.pyplot as plt
pic = io.imread('D.tacos2.jpg')
pic.shape
type(pic)


plt.imshow(pic)
plt.show()

pic_slice = pic[300: , 250:, :]
plt.imshow(pic_slice)
plt.show()

x1, x2 = np.split(pic, 2)
plt.imshow(x1)
plt.show()

plt.imshow(x2)
plt.show()

y1, y2 = np.split(pic, 2,axis = 1)

plt.imshow(y1)
plt.show()

plt.imshow(y2)
plt.show()

# concatenate 
plt.imshow(np.concatenate((x1,x2)))
plt.show()

test = np.array([[ 52,  56,  67],
                   [ 50,  54,  65],
                   [ 50,  52,  64]])
plt.imshow(test)
plt.show()

# shallow copies
places = np.array(['Mexico','China','Janpa','Spain','Europe','Australia'])
loc_1 = places.view()
loc_2 = places.view()

# get false because they all have different id's
loc_1 is places
loc_2 is places
# all three print the same thing.
# point to the same location in memory as they are objects
loc_1.base is places
loc_1[3] = 'Ghana'
# all 3 are affected via views. Reasign the variable or reshpae does not 
# affect the others
print(places)
print(loc_1)
print(loc_2)

# deep copies, no link between original and the copy
loc = places.copy()
loc is places
loc.base is places  # because of the deep copy

loc[0] = 'Turkey'
print(loc)
print(places)

loc.shape = (2,3)

"""
Index masks
---------------------------------------------------------------------
"""

x = np.arange(14) ** 2
print(x)
# print individually
print(x[3], x[7], x[13]) 

# or use a mask and array
mask1 = [1, 3, 7, 13]
print(x[mask1])

mask2 = np.array([[3,5], [2,5]])
print(x[mask2])

cities = np.array([['Sydney','Auckland','Vancouver',],
                   ['Lima', 'Bogota', 'Lisbon'],
                   ['IStanbul', 'Tehran', 'Colombo']])

# 2 masks
row = np.array([[0,0],[2,2]])
col= np.array([[0,2],[0,0]])

cities[row, col]

# can also modify 1d arrays with a mask
cities[row, col] = 'aaaa'
print(cities)

countries = pd.read_csv('countries_of_the_world.csv', decimal=',')
countries.head()
birthrates = countries['Birthrate'].values # values to access individual values
type(birthrates)
birthrates.shape

plt.plot(birthrates)
plt.show()

# nan values
np.median(birthrates)
print(birthrates)

# how to handle nan values
# 1. eliminate the row where nan exists
birthrates2 = birthrates[~np.isnan(birthrates)]
print(birthrates2)

# 2. substitute values as well

"""
Boolean Masks
---------------------------------------------------------------------
"""
x = np.arange(12).reshape(3,4)
index_bool = x > 6
x[index_bool]

np.count_nonzero(x < 7)

np.sum(x<7, axis=1) # axis = 1 is rows
np.sum(x < 7 , axis = 0)

np.any(x > 8) # checks if at least one number is > 8
np.all(x < 11) # checks if all are < 11
    

"""
Structrued arrays
---------------------------------------------------------------------
"""

names = ['Danielle','Lorena','Manuel','Ryan','Teresa','Wes']
ids = [1,2,3,4,5,6]
scores = [78.2 ,57.5, 90, 77, 96.20, 87.37] 


data = np.zeros(6, dtype = {'names': ('Name', 'ID', 'Score'),
                            'formats':('U16', 'i4', 'f8')})

# U16 is for string characters
# i4 is 4-byte int int32
# fu is 8-byte float64

data['Name'] = names
data['ID'] = ids
data['Score'] = scores
# is a list of tuples
print(data)

data[data['Score'] > 85 ]['Name']
data[data['Score'] < 75]['Name']


"""
---------------------------------------------------------------------
Array Broadcasting
Allows arrays of diff. shapoes to be combined.
Memory efficient as needles copies avoided
Shapes should be compatible, compare from last dimension to first.
Dimensions are comaptible if:
    -They are identical
    -one of the dimensions is 1
"""
# Arrays that don't share the same dimensions
# The smaller array is broadcast across the larger array so that they have
# Compatible shapes

# Broadcasting Scalars
# Operations b/w scalara and arrays are always possible - the scalar is broadcast
# over the array

# Broadcasting arrays
# Operations b/t two arrays are possible only incer certain conditions


x = np.array([2,4,6,8,10])
y = np.array([5,5,5,5,5])

x * y

z = 10
x * z

ones = np.ones(shape = (3,4))

ones * z

speed = [184,243,192,309,257,218]
weight = [1178,1243,1403,1047,1673,1475]

car_info = np.array([speed, weight])
print(car_info)

convertion = np.array([0.621371, 2.20462])

car_info * convertion

# reshape convertion
new_convert = convertion.reshape(2,1)
car_info * new_convert
    

### Excercise ###

arr20 = np.arange(90, 300, 2)

x2 = np.arange(0,21,1)

x = arr20[arr20 > 100]

# sub_ar_3 = np.array([[x2 <= 6], [x2 >= 7 & x2 <= 16], [x2 >= 17 & x2 <= 19]])
a,c,b = np.split(x2, [7,17])


cubes = np.array([1,2,3,4,5,6,7,8,9,10]) ** 3
mask4 = np.array([[4,5],[1,2]])
cubes[mask4]

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


