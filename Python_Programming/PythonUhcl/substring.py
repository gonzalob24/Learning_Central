string1 = "abcd"
tempString = ""


def substring(string1):
    tempString = ""
    count = 0
    for letter in string1:
        if letter in tempString:
            continue
        else:
            tempString += letter
            count += 1
    print(tempString + " " + str(count))


substring("abcc")
substring("wwexdw")
substring("bbbbbb")
substring("abccdefg")

