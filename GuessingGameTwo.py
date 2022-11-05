# https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

ans = 'No'
list = []
count = 0

for i in range(1, 101):
    list.append(i)

while ans.lower() != 'yes':
    count += 1
    a = input(str(list[(len(list)//2) - 1]) +
              " Too low or Too High? Or is that your number: ")
    if a.lower() == 'too low':
        list = list[((len(list)//2)):]
        if len(list) == 1:
            print("Thats your number: " + str(list))
            ans = 'yes'

    elif a.lower() == 'too high':
        list = list[:((len(list)//2))]
        if len(list) == 1:
            print("Thats your number: " + str(list))
            ans = 'yes'
    elif a.lower() == ("yes"):
        print("Thats your number: " + str(list[(len(list)//2) - 1]))
        ans = 'yes'
print("It took " + str(count) + " steps")
