# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


how_many = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if how_many <= 0:
    print("Please enter a positive value:")
elif how_many == 1:
    print("Fibonacci sequence upto", how_many, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < how_many:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
