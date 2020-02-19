# Write a program that allows the user to enter a string. It then prints a table of
# the letters of the alphabet in alphabetical order which occur in the string
# together with the number of times each letter occurs. Case should be ignored.
# A sample run of the program might look this this:


import string

sentence = 'ThiS is String with!! Upper and lower case Letters'

strng = sentence.lower().split()
strng = "".join(strng)
print(strng)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

empty_dict = {}

for c in strng:
    if c not in string.punctuation:
        empty_dict[c] = empty_dict.get(c, 0) + 1

for k in sorted(empty_dict.keys()):
    print(k, empty_dict[k])
