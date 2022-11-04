# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def reverse_word_order():
    reverse_word = input("Write a sentence u want to reverse: ")
    res = reverse_word.split()
    res.reverse()
    print(res)


# Created answer is presented as a list, if you want to change that dont use reverse command, after spliting.
reverse_word_order()
