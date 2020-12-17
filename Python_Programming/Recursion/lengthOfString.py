def getLength(string):
    if string == "":
        return 0

    return 1 + getLength(string[1:])


print(getLength("Gonzalo"))
