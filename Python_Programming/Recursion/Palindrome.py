def is_palindrome(pal_string):
    if len(pal_string) <= 1:
        return True
    else:
        return pal_string[0] == pal_string[-1] and is_palindrome(pal_string[1:-1])


def pal(strng):
    if len(strng) == 0:
        return strng
    else:
        return pal(strng[1:]) + strng[0]


x = 'kayak'
print(x[1:-1])
print(pal(x))

