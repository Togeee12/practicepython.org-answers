# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random
i = random.randint(1, 9)
count = 1

a = int(input("Please try to guess a number: "))

while a != i:

    if a < i:
        print("Too low")
    elif a > i:
        print("Too high")
    count += 1
    a = int(input("Please guess a number: "))

print(f"It took you {count} times to guess a number ({i})")
