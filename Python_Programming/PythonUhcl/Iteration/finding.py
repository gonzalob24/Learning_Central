import sys
import string

# punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_'{|}~"


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def find(strng, ch, start=0, end=None):
    index = start
    if end is None:
        end = len(strng)
    while index < end:
        if strng[index] == ch:
            return index
        index += 1
    return -1


def test(did_it_pass):
    line_num = sys._getframe(1).f_lineno
    if did_it_pass:
        msg = "Test at line {0} ok".format(line_num)
    else:
        msg = "Test at line {0} FAILED.".format(line_num)
    print(msg)


def testsuite():
    ss = "Python strings have some interesting methods."
    test(find(ss, "s") == 7)
    test(find(ss, "s", 8) == 13)


fruit = 'Banana'
ss = "Python strings have some interesting methods."
ss2 = "Python?, strings hav{e some interesting methods."
# fruit[0] = 'b' recall strings are immutabl
# lists are mutable
print(list(enumerate(fruit)))

testsuite()
print(ss.find("some"))
print(ss.split())
test1 = remove_punctuation(ss2)
print(test1)
