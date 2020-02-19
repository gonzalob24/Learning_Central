print("Problem 10.14")

'''

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')
'''

# Write a function replace(s, old, new) that replaces all occurences of
# old with new in a string s:

# This is good style of code


def indexall(lst, value):
    return [i for i, v in enumerate(lst) if v == value]


idxall = indexall("MIssIssIppI", "I")
print("Short cut")
print(idxall)


def index2(s, value):
    temp = enumerate(s)
    i = 0
    for i, v in temp:
        if v == value:
            return i


print(index2("Mississippi", "i"))


def my_index(s, chr):
    temp = list(s)
    print(temp)
    idx = ""
    for i in range(len(temp)):
        if temp[i] == chr:
            idx += str(i) + " "

    print(idx)


my_index("Mississippi", "i")

print("\n")


def replace_old(s, old, new):
    temp = list(s)
    # print(temp)
    for i in range(len(temp)):
        if temp[i] == old:
            temp[i] = new
    s = ""
    for i in temp:
        s += str(i)
    ss = "".join(temp)
    print(ss)



def replace(s, old, new):
    temp = s.split(old)
    print(temp)
    print(new.join(temp))


replace("Mississippi", "i", "I")
#replace_old("Mississippi", "i", "I")
s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
replace('Bookkeeper', 'e', 'A')
