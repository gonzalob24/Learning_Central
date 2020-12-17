def removeDuplicates(string):
    if len(string) == 1:
        return string

    if string[0] == string[1]:
        return removeDuplicates(string[1:])

    return string[0] + removeDuplicates(string[1:])


print(removeDuplicates("Helloo"))
