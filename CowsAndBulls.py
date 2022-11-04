# https://gist.github.com/irethoronar/1a8e30ec56c37dd718fc3dc5924ec16b

import random


def cows_n_bulls():
    print("Welcome to the Cows and Bulls Game!")
    a = str(random.randint(1000, 9999))
    print(a)
    cows = 0
    while cows != 4:
        cows = 0
        bulls = 0
        b = input("Please enter a number: ")
        for i in range(4):
            if (b[i] in a) and b[i] == a[i]:
                cows += 1
            elif (b[i] in a) and b[i] != a[i]:
                bulls += 1
        print("Cows: " + str(cows), "Bulls: " + str(bulls))


cows_n_bulls()
