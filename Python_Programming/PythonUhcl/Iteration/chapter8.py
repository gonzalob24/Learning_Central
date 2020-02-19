import sys
import string


def test(did_pass):
    linenum = sys._getframe(1).f_lineno  # gets the caller line num
    if (did_pass):
        msg = "Test at line {0} ok".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)
    print(msg)


def test_suite():
    test(exercise1)


def exercise1():
    #"Python" [1]
    "Strings are sequences of characters." [5]


def modify():
    prefixes = "JKLMNOPQ"
    sufix = "ack"
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "U" + sufix)
        else:
            print(letter + sufix)


def count_letters(stuff, letter):
    count = 0
    for char in stuff:
        if char == letter:
            count += 1
    print("There are " + str(count) + " characters.")

# counts the words in sentence(s) and also the number of "e" in the sentencs(s)


def count_words(paragraph):
    words_without_punctuation = ""
    count_words = 0
    for letter in paragraph:
        if letter not in string.punctuation:
            words_without_punctuation += letter
    words_list = words_without_punctuation.split()
    count_e = 0
    for word in words_list:
        count_words += 1
        if "E".lower() in word:
            count_e += 1
    percent_e = (count_e / count_words) * 100
    print("There are " + str(count_words) + " words, of which " + str(count_e) + " ({0:.2f}".format((percent_e)) + ") contains an e")
    return words_list


def time_table(number1, number2):
    layout = "{0:0}{1:5}{2:5}{3:5}{4:5}{5:5}{6:5}{7:5}{8:5}{9:5}{10:5}{11:5}"
    print(layout.format("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
    print("_____________________________________________________")
    for number1 in range(1, number2 + 1):
        print(layout.format(number1 * 1, number1 * 2, number1 * 3, number1 * 4, number1 * 5, number1 * 6, number1 * 7, number1 * 8, number1 * 9, number1 * 10, number1 * 11, number1 * 12))


def reverse(word):
    word_empty = ""
    for i in word:
        word_empty = i + word_empty
    print(word_empty)


def reverse2(word):
    word_empty = ""
    for i in word:
        word_empty = i + word_empty
    print(word + " " + word_empty)


def counts(what, word):  # counts how how many times "what" appears in words
    count = word.count(what)
    print(count)


counts("Mis", "Mississippi")
# reverse2("good")
reverse2("Python")
reverse('happy')

# time_table(1,12)

sentence = """
Pythons are constrictors, which means that they will ’squeeze’ the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake’s
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The ’extra stuff’ gets passed out as ---
you guessed it --- snake POOP! """
s = count_words(sentence)
# print(s)


# count_letters("Oranage","a")
# modify()
# test_suite()
