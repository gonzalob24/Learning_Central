def removeSpaces(string):
    # base case
    if string == "":
        return ""

    if string[0] == " " or string[0] == "\t":
        return removeSpaces(string[1:])
    return string[0] + removeSpaces(string[1:])


print(removeSpaces("Hey Gonzalo"))
print(removeSpaces("Hey\tGonzalo"))
