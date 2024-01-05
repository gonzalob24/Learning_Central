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