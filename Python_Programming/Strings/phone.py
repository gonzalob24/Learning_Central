import re

# compile( ), search( ), and group( ).

def isPhoneNum(text):
    """" returns True if pattern of phone number is found """
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != "-":
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# print("713-456-7890 is a phone number:")
# print(isPhoneNum("713-456-7890"))
# print("713-4567-789 is a phone number: ")
# print(isPhoneNum("713-4567-789"))


message ="Call me at 409-123-1234. If I don’t answer, try 281-987-6543. Thanks"

# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNum(chunk):
#         print("Phone number: " + chunk)


r1 = re.compile(r'\d{3}-\d{3}-\d{3}')
r2 = re.compile(r'55+')
address = re.compile(r'.*')
mo = r1.search('Here is a number: 555-123-1234 and 456-789-1233')
mo2 = r2.search('Here is a number: 555-123-1234')
mo3 = address.search('gonzalobetancourt@me.com')
print(type(mo))
print(mo.group())
print(mo2.group())
print(mo3.group())
print("Done")
