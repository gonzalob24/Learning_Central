def mergeStrings(str1, str2):
    if str1 == "" or str2 == "":
        return str1 + str2

    if str1[0] < str2[0]:
        return str1[0] + mergeStrings(str1[1:], str2)
    return str2[0] + mergeStrings(str1, str2[1:])


print(mergeStrings("acu", "bst"))
print("D" < "a")
