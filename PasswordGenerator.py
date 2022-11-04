# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random as rd
import secrets as sc
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = int(input("Please enter length of generated password: "))


pwd = ''

for i in range(pwd_length):
    pwd += ''.join(sc.choice(alphabet))

print(pwd)
