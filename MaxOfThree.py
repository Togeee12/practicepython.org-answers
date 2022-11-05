def greatestof3numbers():
    numbers = input('Type your 3 different numbers with spaces: ')
    numlist = numbers.split()
    num1 = int(numlist[0])
    num2 = int(numlist[1])
    num3 = int(numlist[2])
    if num1 > num2:
        if num1 > num3:
            print(num1, 'is greatest of 3.')
        else:
            print(num3, 'is greatest of 3.')
    elif num1 == num2 and num3 == num2:
        print("Numbers are equal!")
    else:
        if num2 > num3:
            print(num2, 'is greatest of 3.')
        else:
            print(num3, 'is greatest of 3.')


greatestof3numbers()
