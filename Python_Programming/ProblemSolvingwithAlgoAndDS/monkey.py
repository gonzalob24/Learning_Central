import random


def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for i in range(strlen):
        result = result + alphabet[random.randrange(27)]

    return result

def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return numSame / len(goal)

print(score("methinks it si like a weasel", generateOne(28)))


def  main():
    goalstring = "methinks it si like a weasel"
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore >= best:
            print(newscore, newstring)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)
main()
