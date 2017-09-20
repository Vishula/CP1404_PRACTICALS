"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
(Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels)
"""
import random

__Author__ = 'Vishula Gamaetige'
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"
letters = "aeioubcdfghjklmnpqrstvwxyz"
numbers =  "0123456789"
password = ""
error = False
hasAll = False # check to see if string has all required types (eg. numbers, upper/lower characters, etc.)
count_lower = 0
count_upper = 0
count_digit = 0
count_special = 0


print("How many characters do you want in your password?")
strLen = int(input("> "))
print("\nDo you want any of the following in your password (y or n):\n")

uppr = str(input("\tUppercase characters?\n \t> "))
lwr = str(input("\tLowercase characters?\n \t> "))
num = str(input("\tNumeric characters?\n \t> "))
spec = str(input("\tSpecial characters?\n \t> "))



while len(password) < strLen:
    z = random.randint(1,4)
    if (z == 1 and uppr == "y" and count_upper < 1) or (hasAll is True and z == 1):
        password += random.choice(letters.upper())
        count_upper += 1
    elif (z == 2 and lwr == "y" and count_lower < 1) or (hasAll is True and z == 2):
        password += random.choice(letters.lower())
        count_lower += 1
    elif (z == 3 and num == "y" and count_digit < 1) or (hasAll is True and z == 3):
        password += random.choice(numbers)
        count_digit += 1
    elif (z == 4 and spec == "y" and count_special < 1) or (hasAll is True and z == 4):
        password += random.choice(SPECIAL_CHARACTERS)
        count_special += 1
    elif hasAll is False and (count_lower == 1 or count_upper == 1 or count_digit == 1 or count_special == 1):
        hasAll = True

print("Password is: " + password)
# Counting types is done when generating password
# Check if password is valid or not
if not 5 <= int(len(password)) <= 15:
    error = True
elif count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
    error = True
# check if error
if error:
    print("Invalid password!")
else:
    print("Valid password!")