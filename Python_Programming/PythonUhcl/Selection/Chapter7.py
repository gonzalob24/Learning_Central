#The first six questions are typical functions you should be able to write using only these building blocks.

#Write a function to count how many odd numbers are in a list.  XXX

#Sum up all the even numbers in a list. XXX

#Sum up all the negative numbers in a list. XXX

#Count how many words in a list have length 5.  XXX

#Write a function, is_prime, which takes a single integer argument and returns True when the argument is a prime 
#number and False otherwise. Add tests for cases like this:

#Sum all the elements in a list up to but not including the first even number. (Write your unit tests. What 
#if there is 
#no even number?)

#Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your 
#unit #tests for this case too. What if “sam” does not occur?)

#Add a print function to Newton’s sqrt function that prints out better each time it is calculated. Call your 
#modified #function with 25 as an argument and record the results.

#Trace the execution of the last version of print_mult_table and figure out how it works.

#Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A call to 
#print_triangular_numbers(5) would produce the following output:

#1       1
#2       3
#3       6
#4       10
#5       15

import sys

#kees track of how many odd numbers are in the list
def oddNumbs(ls):
    countEven = 0
    for number in ls:
        if number % 2 == 0:
            countEven += 1
    return countEven

#sums up only the even numbers in the list
def sumEven(ls):
    sumAll = 0
    for number in ls:
        if number % 2 == 0:
            sumAll += number
    return sumAll

#sum of negative numbers in a list
def sumNeg(ls):
    sumAll = 0
    for number in ls:
        if number < 0:
            sumAll += number
    return sumAll

#counts how many words in a list have length 5
def wordCount(words):
    count = 0
    for word in words:
        if len(word) == 5:
            count += 1
    return count

#return true when prime and false when not prime
def is_prime(number):
    increment = 2
    track = 0
    while increment < number:
        if number % increment == 0:
            return False
            break
        else: #number % increment != 0
            increment += 1
    return True
##test cases

def test(did_pass):
    linenum = sys._getframe(1).f_lineno #get line number where test took place
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)
#test suite
def test_suite():
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))

test_suite()

ls = [1,2,3,4,30,22,100,103,202]
print(oddNumbs(ls))

x = [2,4,3,5,20]
print(sumEven(x))

w = [-1,-20,10,-2]
print(sumNeg(w))

test = ["hello", "mom", "balls", "running", "earth"]
print(wordCount(test))

print(is_prime(11))
print(not is_prime(35))
print(is_prime(19911121))

#print(is_prime(12))
#test_suite()






