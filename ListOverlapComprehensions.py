# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random as rd

a = [rd.randint(1, 100) for i in range(0, 10)]
b = [rd.randint(1, 100) for n in range(0, 10)]

print(a, "\n", b)
l1 = [item for item in a if item in b]
print(l1)
