# Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

# dict. with the translations
eng2pir = {'sir':'matey', 'hotel':'fleabag inn', 'student':'swabbie', 'boy':'matey', 'madam':'proud beauty',
           'professor':'foul blaggart', 'restaurant':'galley', 'your':'yer', 'excuse':'arr',
           'students':'swabbies', 'are':'be', 'lawyer':'foul blaggart', 'the':'th\'',
           'restroom':'head', 'my':'me', 'hello':'avast', 'is':'be', 'man':'matey'}


strng_input = input('Enter a sentence: ')

def translate(strng_input):
    for word in strng_input.split(): #puts sentence in a list.
        strng_new = ""
        if word in eng2pir.keys():
            word = eng2pir[word]
        strng_new += word

        print(strng_new, end=" ")
