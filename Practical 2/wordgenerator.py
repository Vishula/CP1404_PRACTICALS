
import random

__Author__ = 'Vishula Gamaetige'
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word = ""
word_format = ""

y = random.randint(4,8)
#generate word_format between 4 and 8 letters (randomly selected No.'s)
for x in range(0,y):
    #Added some extra %'s to increase the chances of consonants in the string
    word_format += random.choice("%#%*%")
#Convert the words format to letters
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind in "#*":
        word += random.choice(VOWELS)
    elif kind.isalpha():
        word += kind
print("Random word is: " + word)