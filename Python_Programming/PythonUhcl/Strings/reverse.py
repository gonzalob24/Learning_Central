#reverse a string
# we can use the reverse funcion

str1 = 'hello'
str2 = 'follow'
str3 = 'l'


def reverse_str(s):
    if len(s) == 1:
        return s
    else:
        return reverse_str(s[1:]) + s[0]


print(reverse_str(str1))
print(reverse_str(str2))
print(reverse_str(str3))
