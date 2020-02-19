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


def count():
    f = open('aaw.txt', 'r')

    count = {}

    for line in f:
        for word in line.split():

            # remove punctuation
            word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
            word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
            word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
            word = word.replace(']', '').replace(';', '')

            # ignore case
            word = word.lower()

            # ignore numbers
            if word.isalpha():
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1

    keys = count.keys()
    sorted(keys)

    # save the word count analysis to a file
    out = open('alice_words.txt', 'w')

    for word in keys:
        out.write(word + " " + str(count[word]))
        out.write('\n')

    print("The word 'alice' appears " + str(count['alice']) + " times in the book.")

count()
