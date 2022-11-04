# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input("Enter a number: "))
print([n for n in range(1, number+1) if number % n == 0])
