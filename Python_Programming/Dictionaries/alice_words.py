# Write a program called alice_words.py that creates a text file named alice_words.txt
# containing an alphabetical listing of all the words, and the number of times each
# occurs, in the text version of Alice’s Adventures in Wonderland.
import string

fname = open('aaw.txt', 'r')

empty_dict = {}
for line in fname:
    split_line = line.lower().split()
    for word in split_line:
        if word.isalpha():
            if word not in string.punctuation:
                empty_dict[word] = empty_dict.get(word, 0) + 1

for k in sorted(empty_dict.keys()):
    print(k, empty_dict[k])
