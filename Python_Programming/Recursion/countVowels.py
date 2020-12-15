def countVowels(string):
    vowels = 'aeiou'
    if len(string) == 0:
        return 0

    if string[0].lower() in vowels:
        return 1 + countVowels(string[1:])
    return countVowels(string[1:])


print(countVowels('gonzalo'))
print(countVowels('Educative'))
