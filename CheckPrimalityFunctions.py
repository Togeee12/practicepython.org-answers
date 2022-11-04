# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def determine_prime_or_not(number):
    count = 2
    while count < number:
        if number % count == 0:
            return False
        else:
            count += 1
            return True


def main():
    number = int(input("Enter a number to check if it is prime or not: "))
    prime_or_not = determine_prime_or_not(number)
    if prime_or_not:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


main()
