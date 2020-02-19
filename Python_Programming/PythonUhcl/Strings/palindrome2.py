# Write a function that takes a string as a parameter and returns True if the string
# is a palindrome, False otherwise. Remember that a string is a palindrome if it is
# spelled the same both forward and backward. for example: radar is a palindrome.
# for bonus points palindromes can also be phrases, but you need to remove the spaces
# and punctuation before checking. for example: madam i’m adam is a palindrome. Other
# fun palindromes include:
import string

str1 = 'kayak'
str2 = 'aibohphobia'
str3 = 'Live not on evil'
str4 = 'Reviled did I live, said I, as evil I did deliver'
str5 = 'Go hang a salami; I’m a lasagna hog.'
str6 = 'Able was I ere I saw Elba'
str7 = 'Kanakanak – a town in Alaska'
str8 = 'Wassamassaw – a town in South Dakota'


def palindrome(strng):
    if len(strng) == 1 or len(strng) == 0:
        return strng
    else:
        result = ''   # An empty string
        for word in strng.lower():
            if word not in string.punctuation:
                result += word
        final_str = "".join(result.split())
        return palindrome(final_str[1:]) + final_str[0]


print(palindrome(str8))


def p(s):
    newp = s[::-1]
    newp = "".join(newp.split())
    s = "".join(s.split())
    if s == newp:
        return True;
    else:
        return False



print(p(str8))
print(p(str1))
print(p(str2))
print(palindrome("The"))
