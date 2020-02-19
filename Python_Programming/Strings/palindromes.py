# program that checks if a word or sentence is a palindrome. 

first = "a man a plan a canal panama"

# function that checks if the string is a palindrome
def is_palindrome(s):
    # empty string that will hold the reversed string
    reverse = ""  
    # splits the original string and then joins it without spaces
    new_string = "".join(s.split())
    print(new_string)
    for c in range(len(new_string)):
        # reverses the new_string
        reverse = new_string[c] + reverse
    if new_string == reverse:
        return True
    else:
        return False


print(is_palindrome(first))

#short hand notation to reverse a string
# txt = "a man a plan a canal panama"[::-1]
#print(txt)
