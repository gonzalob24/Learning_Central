#Finding Numbers in a Haystack

#In this assignment you will read through and parse a 
#file with text and numbers. You will extract all the 
#numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment. One is a sample 
#file where we give you the sum for your testing and the 
#other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt 
#(There are 90 values with a sum=445833)

#Actual data: http://py4e-data.dr-chuck.net/regex_sum_170778.txt 
#(There are 94 values and the sum ends with 135)

#These links open in a new window. Make sure to save the 
#file into the same folder as you will be writing your Python 
#program. Note: Each student will have a distinct data file 
#for the assignment - so only use your own data file for analysis.

#Data Format
#The file contains much of the text from the introduction of 
#the textbook except that random numbers are inserted throughout 
#the text. Here is a sample of the output you might see:

#Sum of actual data ends in 135


import re

fname = input("Enter the name of the file: ")
fopen = open(fname)
lst = list() #creating an empty list

#read each line of the file
for line in fopen:
	line = line.strip() #strip the new line characters
	#in the current line we only need to read the digits including
	#repeating numbers one or more times
	y = re.findall('[0-9]+', line) #re.findall extracts portions of a string that match my re
	#if y is empty continue do not append
	if y == []:
		continue
	#for loop to extract each number as an integer from each line
	for i in range(len(y)):
		num = int(y[i]) #assign each number from the extracted line as an integer
		lst.append(num) #append each num to the empty list

print(sum(lst), ", length of lst is", len(lst)) 

