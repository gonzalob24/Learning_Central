import random
rand = random.Random()

# Create a guessing game
number = rand.randrange(1, 1000)
guesses = 0
msg = ""
# while True:
#   guess = int(input('Guess a number between 1 and 1000: '))
#   guesses += 1
  
#   if guess > number:
#     msg = "{0} is too high. \n".format(guess)
#   elif guess < number:
#     msg = "{0} is too low. \n".format(guess)
#   else: 
#     break
#   print(msg)

# print(f'\n\nGreat you got it in {guesses} of guesses')

# Paired Data
year_born = ("Alexa", 2013)
# similar to JS destructuring
(name, year) = year_born 
print(*year_born)
print(name)

"""
  11 - Lists
"""
a = "banana"
b = "banana"
if a is b:
  print('yes as is b')
else: 
  print('No') 
  
if a == b:
  print('yes')
else: 
  print('No')
  
# Cloning a List
a = [1,2,3,4]
a_clone = a[:]
print(a[:])

# List parameters
print(enumerate(a))

# inpt = input('Something: ')
# print(inpt.strip())

al = [1, 2, 3, [3, 4, [5, 6, 7]]]

a2 = al[:]
print(a2)
print(al is a2)