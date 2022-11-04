# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

input_number = int(
    input("Insert a number which will be checked if its odd or even. "))
if input_number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
