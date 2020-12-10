def canConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return memo[target]

    memo[target] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(canConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(canConstruct("enterpotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                   ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {}))

# g = 'Gonzalo'
# print(g.index('x') == 0)
# print(g.find('x') == 0)
