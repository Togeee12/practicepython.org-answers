# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

date = datetime.datetime.now().year
name = input("What is your name? ")
age = int(input("What is your age? "))
age100 = (date - age) + 100
print(f"{name}, you will turn 100 years old int the year {age100}")

# :D
