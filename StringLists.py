# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

def palindrome(i):
    return i == i[::-1]


input_string = input("Please enter any words: ")
if palindrome(input_string):
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")
