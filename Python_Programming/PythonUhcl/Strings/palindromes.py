first = "a man a plan a canal panama"


def is_palindrome(s):
    reverse = ""
    new_string = "".join(s.split())
    print(new_string)
    for c in range(len(new_string)):
        #temp = new_string[c]
        #for letter in temp:
        reverse = new_string[c] + reverse
    print(reverse)
    if new_string == reverse:
        return True
    else:
        return False






print(is_palindrome(first))
print("____________")
txt = "a man a plan a canal panama"[::-1]
print(txt)
