# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random as rd


def common_item(listA, listB):
    c = []

    for number in listA:
        if number in listB:
            if number in c:
                continue
            c.append(number)
            return c


def creating_list():
    random_list = []
    list_size = rd.randint(5, 6)
    for number in range(list_size + 1):
        random_list.append(rd.randint(1, 100))
    return random_list


def main():
    A = creating_list()
    B = creating_list()
    result = common_item(A, B)
    print(f"List A: {A}")
    print(f"List B: {B}")
    print()
    if result:
        print(f"Common numbers between List A and List B are: {result}")
    else:
        print("There are no common numbers between the lists.")


main()
