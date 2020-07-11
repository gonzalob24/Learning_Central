import sys, string, collections


def animal_crackers(str1):
    """
        ANIMAL CRACKERS: Write a function takes a two-word string and returns True if
        both words begin with same letter¶
    """
    str1 = str1.split(" ")
    if str1[0][0] == str1[1][0]:
        return True
    else:
        return False


def cap_name(name):
    """"
        LD MACDONALD: Write a function that capitalizes the first and 
        fourth letters of a name:
    """
    return name[:3].capitalize() + name[3:].capitalize()


def reverse_sentence(sentence):
    sentence = " ".join(sentence.split(" ")[::-1])
    return sentence


def increase_string(word):
    result = ""
    for ch in word:
        result += ch * 3
    return result



def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def almost_ther(num):
    if abs(100 - num) <= 10 or abs(200 - num) <= 10:
        return True
    else:
        return False


def spy_game(lst):
    """
    Write a function that takes in a list of integers and returns
    True if it contains 007 in order
    """
    code = [0, 0, 7, 'k']
    for n in lst:
        if n == code[0]:
            code.pop(0)
    return len(code) == 1


def count_primes(num):
    primes = [2]
    p = 3
    if num < 2:
        return 0

    while p <= num:
        for y in primes:
            if p % y == 0:
                p += 2
                break
        else:
            primes.append(p)
            p += 2
    print(primes)
    return len(primes)


def unique_list(list1):
    """
    Write a Python function that takes a list and returns a new list with
    unique elements of the first list.
    """
    return list(set(list1))


def is_pangram(strng1, alphabet=string.ascii_lowercase):
    """
    Write a Python function to check whether a string is pangram or not.
    Pangrams are words or sentences containing every letter of the alphabet
    at least once
    :param strng1:
    :param alphabet:
    :return:
    """
    # strng1 = list(set("".join(strng1.split(" ")).lower()))
    # result = ""
    # strng1.sort()
    # strng1 = "".join(strng1)
    # return strng1 == alphabet

    # BETTER SOLUTION

    alphaset = set(alphabet)
    return alphaset <= set(strng1.lower())


def up_low(strng):
    d_low_up = {"upper": 0, "lower": 0}
    for ch in strng:
        if ch.isupper():
            d_low_up["upper"] += 1
        elif ch.islower():
            d_low_up["lower"] += 1
        else:
            pass
    print("Number of uppercase is : ", d_low_up["upper"])
    print("Number of lowercase is : ", d_low_up["lower"])

def up_low2(strng):
    count = collections.Counter(strng)
    print(count.most_common())

    # print("Number of uppercase is : ", d_low_up["upper"])
    # print("Number of lowercase is : ", d_low_up["lower"])
    return list(count)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(animal_crackers("Hello Hi") is True)
    test(animal_crackers("Crazy Kangaroo") is False)
    assert animal_crackers("hi ti") is False
    test(cap_name("gonzalo") == "GonZalo")
    test(cap_name("macdonalds") == "MacDonalds")
    print("\nreverse_sentence() tests")
    test(reverse_sentence("I am home") == "home am I")
    test(reverse_sentence("We are ready") == "ready are We")
    print("\nalmost_there tests")
    test(almost_ther(90) is True)
    test(almost_ther(201) is True)
    test(almost_ther(210) is True)
    print("\nincrease string tests")
    test(increase_string("hello")) == "hhheeelllooo"
    test(increase_string("Mississippi")) == "MMMiiissssssiiissssssiiippppppiii"
    print("\nspy game tests")
    test(spy_game([1, 2, 3, 0, 0, 7, 5]) is True)
    test(spy_game([1, 7, 1, 0, 7, 5, 0]) is False)
    test(count_primes(100) == 25)
    print("\nUnique list problem")
    test(unique_list([1,1,1,1,2,2,2,2,3,3,4,4]) == [1, 2, 3, 4])
    test(unique_list(unique_list([1,1,1,1,2,2,3,3,3,3,4,5])) == [1, 2, 3, 4, 5])
    test(is_pangram("The quick brown fox jumps over the lazy dog") is True)
    print("\nNumber of Lower and Upper case letters.")
    up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
    test(is_pangram("Gonzalo is good at basketball") is False)
    test(is_pangram("The quick brown fox jumps over the lazy dog") is True)
    test(is_pangram("The basketball") is False)

if __name__ == "__main__":
    # test_suite()

    print(up_low2("Hello Mr. Rogers, how are you this fine Tuesday?"))
