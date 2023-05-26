from copy import deepcopy
import collections
import json

arr1 = [1,2,3,4,5,6,7, [[100]]]
arr2 = [9, 8]
temp = arr1[3:6]

print(arr1)
print(temp)
temp[0] = 10
print(arr1)
print(temp)

arr1.extend(arr2)
print(arr1)
arr2[0] = 99
print(arr1)
arr3 = deepcopy(arr1)
arr4 = list(arr1)
print(arr3)
arr1[7][0] = 200
print("arr4: ", arr4)


# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written 
# using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

def isAnagram(string1, string2):
  string1Array = " ".join(string1.lower()).split()
  string2Array = " ".join(string2.lower()).split()
  
  for letter1 in string1Array:
    if letter1 in string2Array:
      return True
    else:
      return False

def isAnagram2(str1, str2):
  str1Array = str1.replace(' ', '').lower()
  str2Array = str2.replace(' ', '').lower()
  
  count = {}
  
  # Edge Case
  if len(str1Array) != len(str2Array):
    return False
  
  for letter in str1Array:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1
      
  print("count: ",  count)
  
  for letter in str2Array:
    if letter in count:
      count[letter] -= 1
    else:
      count[letter] = 1
  
  print(count)
  for k in count:
    if count[k] != 0:
      return False
  
  return True
  
  
# print(isAnagram("Gonzalo", "Lonzgao"))
# print(isAnagram('dog','god'))
# print(isAnagram('clint eastwood','old west action'))
# print(isAnagram('aa','bb'))

# print(isAnagram2("Gonzalo", "Lonzgao"))
# print(isAnagram2('dog','god'))
# print(isAnagram2('clint eastwood', 'old west action'))
# print(isAnagram2('aa','bb'))


#########
# Given an integer array, output all the ** unique ** pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return 2 pairs:

#  (1,3)
#  (2,2)

def pair_sum(arr, n):
  sumPairs = set()
  # i = 0
  # j = 1
  # loop from j to n
  #  check if i + j = 4
  #     if true append (i, j) to sumPairs
  
  for i in range(len(arr) - 1):
    # print("i: ", i)
    for j in range(i + 1, len(arr)):
      # print("j: ", j)
      if arr[i] + arr[j] == n:
        sumPairs.add((arr[i], arr[j]))
  
  return sumPairs

# Better solution
def pair_sum3(arr, k):
  seenNumbers = set()
  output = set()
  
  if len(arr) < 2:
    return
  
  for num in arr:
    target = k - num
    
    if target not in seenNumbers:
      seenNumbers.add(num)
    else:
      output.add((min(num, target), max(num, target)))
      
  return len(output)
    


# print(pair_sum([1,3,2,2],4))
# print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
# print(pair_sum3([2,3,6,8,7], 10))

# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

# Input:

# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

# Output:

# 5 is the missing number

def findMissingNum(arr1, arr2):
  # missingNum = None
  
  # n^2
  for num in arr1: # n
    if num not in arr2: # n
      return num

def findMissingNum2(arr1, arr2):
  numsInArray = {}
  d = collections.defaultdict(int)
  print("dict: ", d)
  
  for num in arr2:
    d[num] += 1
  
  print("dict: ", d)
  
  for num in arr1:
    if num not in numsInArray:
      numsInArray[num] = num
  
  for num in arr2:
    if num in numsInArray:
      del numsInArray[num]
      
  print(numsInArray)
  return next(iter(numsInArray))

# print("Missing: ", findMissingNum2([1,2,3,4,5,6,7], [3,7,2,1,4,6]))

# Given an array of integers (positive and negative) find the largest continuous sum.

# [1,2,-1,3,4,-1]),9
# [1,2,-1,3,4,10,10,-10,-1]),29
# [-1,1]),1

def largestContinuousSum(arr):
  maxSum = 0
  
  # time complexity --> n^2
  for i in range(len(arr) - 1): # n
    tempSum = 0
    tempSum = arr[i]
    for j in range(i + 1, len(arr)): # n
      tempSum += arr[j]              # n * n
      if tempSum > maxSum:
        maxSum = tempSum
    
  return maxSum

def largestContinuousSum2(arr):
  maxSum = 0
  tempSum1 = 0
  tempSum2 = 0
  
  # time complexity --> n + n + n = 3n --> O(n)
  for i in range(len(arr)): # n
    tempSum1 += arr[i]
    tempSum2 += arr[i]
  
  maxSum = tempSum1          # 1
  
  for i in range(len(arr)):  # n
    tempSum1 -= arr1[i]      # n
    
    if tempSum1 > maxSum:    # n
      maxSum = tempSum1
  
  for i in range(len(arr) - 1, -1, -1): # n
    tempSum2 -= arr[i]  # n
    if tempSum2 > maxSum:
      maxSum = tempSum2
    
  return maxSum

def largestContSum(arr):
  if len(arr) == 0:
    return 0
  
  maxSum = currentSum = arr[0]
  
  for num in arr[1:]:
    currentSum = max(currentSum + num, num)
    
    maxSum = max(currentSum, maxSum)
  
  return maxSum
 
# print(largestContinuousSum([1,2,-1,3,4,-1]))
# print(largestContinuousSum([1,2,-1,3,4,10,10,-10,-1]))
# print(largestContinuousSum([-8,3,10,3,4]))

# print(largestContinuousSum2([-1,-2,-1,3,-4,-1]))
# print(largestContSum([-1,-2,-1,-3,-4,-1]))

#################

# Given a string of words, reverse all the words. For example:
# Given:

# 'This is the best'

# Return:
# 'best the is This'

# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# '  space here'  and 'space here      '

# both become:
# 'here space'

def reverseSentence(sentence):
  sentenceArr = sentence.strip().split(" ")
  reversedSentence = sentenceArr[len(sentenceArr) - 1].strip()
  for word in sentenceArr[len(sentenceArr) - 2::-1]:
    if word != "":
      reversedSentence = reversedSentence + " " + word.strip()
  
  return reversedSentence
  
  
print(reverseSentence(' gonzalo was    here '))

str = " gonzalo was    here "
print(" ".join(reversed(str.split())))

##############

# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

def compress(s):
  # count = {}
  count = collections.defaultdict(lambda: "Not Present")
  results = ""
  
  for letter in s:
    if letter not in count:
      count[letter] = 1
    else:
      count[letter] += 1

  for item in count:
    results = results + item + f'{count[item]}'
    
  return results 

def compress2(s):
  
  l = len(s)
  count = 1
  result = ""
  
  if l == 0:
    return ""

  if l == 1:
    return s[0] + f'{s[0]}'
  
  for i in range(1, l):
    # print(s[i])
    if s[i] == s[i - 1]:
      # print(s[i])
      count += 1
    else: 
      result = result + s[i - 1] + f'{count}'
      count = 1
  
  result = result + s[i - 1] + f'{count}'
  
  return result   
  
# print(compress2('AAAAABBBBCCCCccc'))

# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

def uniChar(s):
  count = collections.defaultdict(lambda: "Not Present")
  
  if len(s) == 0:
    return True
  
  for letter in s:
    if letter not in count:
      count[letter] = 1
    else:
      count[letter] += 1
  
  for item in count:
    if count[item] != 1:
      return False
    
  return True

def uniChar2(s):
  # One line
  # return len(set(s) == len(s))
  count = set()
  
  for letter in s:
    if letter in count:
      return False
    else:
      count.add(letter)
      
  return True

print(uniChar2('goo'))
print(uniChar2(''))
print(uniChar2('abcd'))