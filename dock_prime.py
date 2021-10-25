from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True
for i in range (1, 500):

    if is_prime(i)==True:

        print(i,end=' ')
