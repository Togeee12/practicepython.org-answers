# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

def return_prime_value():
    with open('primenumberlist.txt', 'r') as open_prime:
        opened = list(open_prime.read().split('\n'))
        return opened


def return_positive():
    with open('happynumbers.txt', 'r') as open_happy:
        opened = list(open_happy.read().split('\n'))
        return opened


one_list = [x for x in return_prime_value if x in return_positive()]
print(one_list)
