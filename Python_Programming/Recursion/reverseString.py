def reverseString(strng):
    if len(strng) == 0:
        return strng

    return reverseString(strng[1:]) + strng[0]


print(reverseString("Gonzalo"))
