import re

patterns = ['term1', 'term2']
text = 'this is a string with term1, but not other term'
# print(re.search('hello', 'hello world'))

for pattern in patterns:
    print('Search for "%s" in: \n"%s"' % (pattern, text))

    # Check for a match
    if re.search(pattern, text):
        print("\n")
        print("match was found")
    else:
        print("\n")
        print("Match was not found")

print("\n\n")
# Splitting with regx

split_term = '@'
phrase = "what is your email, is it hello@gmail.com"
print(re.split(split_term, phrase))

print("\n\n")
# Finding all instances of a pattern
print(re.findall("match", "here is one match, here is another match"))


def multi_re_find(patterns, phrase):
    """
    Takes in a list of regex patterns
    prints a lift of all matches
    :param patterns:
    :param phrase:
    :return:
    """
    for pattern in patterns:
        print("Searching the phrase using the re check: %r" % pattern)
        print(re.findall(pattern, phrase))
        print("\n")


print("\n\nUsing meta chatracters:")
test_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"

test_patterns = ['sd*',  # s followed by zero or more d's
                 'sd+',  # s followed by one or more d's
                 'sd?',  # s followed by zero or one d's
                 'sd{3}',  # s followed by 3 d's
                 'sd{2,3}',  # s followed by by two to three d's
                 ]

multi_re_find(test_patterns, test_phrase)
"""
There are five ways to express repetition in a pattern:
1.A pattern followed by the meta-character * is repeated zero or more times.
2. Replace the * with + and the pattern must appear at least once.
3. Using ? means the pattern appears zero or one time.
4. For a specific number of occurrences, use {m} after the pattern, where m is 
    replaced with the number of times the pattern should repeat.
5. Use {m,n} where m is the minimum number of repetitions and n is the maximum. 
    Leaving out n {m,} means the value appears at least m times, with no maximum.
"""
"""
Character sets:
Are used when you wish to match any one of a group of characters at a 
point in the input. Brackets are used to construct character set inputs. 
For example: the input [ab] searches for occurrences of either a or b. Let's see 
some examples:
"""
test_patterns2 = ['[sd]',  # either s or d
                  's[sd]+']  # s followed by one or more s or d

multi_re_find(test_patterns2, test_phrase)

"""
Exclusion (^)
We can use ^ to exclude terms by incorporating it into the bracket syntax notation. 
For example: [^...] will match any single character not in the brackets. Let's see 
some examples:
"""
'''
Use [^!.? ] to check for matches that are not a !,.,?, or space. 
Add a + to check that the match appears at least once. This basically translates 
into finding the words.
'''
test_phrase3 = 'This is a string! But it has punctuation. How can we remove it?'

print(re.findall('[^!.? ]+', test_phrase3))
print("\n\nCharacter Ranges")
"""
Character Ranges
As character sets grow larger, typing every character that should (or should not) 
match could become very tedious. A more compact format using character ranges 
lets you define a character set to include all of the contiguous characters between 
a start and stop point. The format used is [start-end].
Common use cases are to search for a specific range of letters in the alphabet. 
For instance, [a-f] would return matches with any occurrence of letters between a and f.
Let's walk through some examples:
"""

test_phrase4 = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns4 = ['[a-z]+',  # sequences of lower case letters
                  '[A-Z]+',  # sequences of upper case letters
                  '[a-zA-Z]+',  # sequences of lower or upper case letters
                  '[A-Z][a-z]+']  # one upper case letter followed by lower case letters

multi_re_find(test_patterns4, test_phrase4)

print("\n\nEscape Codes")
"""
Escape Codes
You can use special escape codes to find specific types of patterns in your data, 
such as digits, non-digits, whitespace, and more. For example:
Code	Meaning
\d	a digit
\D	a non-digit
\s	whitespace (tab, space, newline, etc.)
\S	non-whitespace
\w	alphanumeric
\W	non-alphanumeric

Escapes are indicated by prefixing the character with a backslash \. Unfortunately, 
a backslash must itself be escaped in normal Python strings, and that results in 
expressions that are difficult to read. Using raw strings, created by prefixing the 
literal value with r, eliminates this problem and maintains readability.
Personally, I think this use of r to escape a backslash is probably one of the things 
that block someone who is not familiar with regex in Python from being able to read 
regex code at first. Hopefully after seeing these examples this syntax will become clear.
"""

test_phrase5 = 'This is! a string!.? with some numbers 1233 and a symbol #hashtag'

test_patterns5 = [r'\d+',  # sequence of digits
                  r'\D+',  # sequence of non-digits
                  r'\s+',  # sequence of whitespace
                  r'\S+',  # sequence of non-whitespace
                  r'\w+',  # alphanumeric characters
                  r'\W+',  # non-alphanumeric
                  ]

multi_re_find(test_patterns5, test_phrase5)
