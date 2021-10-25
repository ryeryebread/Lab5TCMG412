
import math

a = int(input('please enter an integer: '))

b = int(input('please enter and integer: '))

if a < b or a < 0 or b < 0:
    print()
    print('invalid input')
    exit()


def my_factorial(c):
    n1 = math.factorial(c)

    return n1


def my_combinations(n, k):
    de = my_factorial(n)
    x = my_factorial(n - k)
    y = my_factorial(k)
    nu = x * y
    n2 = de / nu
    return n2


print(str('You can choose'),a,str('objects from'),b,str('objects in'),my_combinations(a,b),str('ways'))
