# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def listA():
    my_list = []
    n = int(input("Enter number of elements: "))
    for i in range(0, n):
        el = int(input("Enter your number: "))
        my_list.append(el)
    print(set(my_list))


listA()
