from flask import Flask, request, jsonify, render_template
import math
from math import sqrt
from itertools import count, islice

app = Flask(__name__)

@app.route('/factorial', methods=["GET"])
def factorial():
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


@app.route('/fibonacci', methods=["GET"])
def fibonacci():
    start_num = int(input('Enter starting number:'))
    end_num = int(input('Enter ending number:'))

    count = 0
    first_fibo = 0
    second_fibo = 1
    third_fibo = 1

    fibo_nums = []

    while True:
        third_fibo = second_fibo
        second_fibo = first_fibo
        first_fibo = first_fibo + third_fibo
        if first_fibo >= start_num and first_fibo <= end_num:
            fibo_nums.append(first_fibo)

        if(first_fibo > end_num):
            break

    print('\nThe {} Fibonacci numbers between {} and {} are:'.format(len(fibo_nums),start_num,end_num))
    result = ''
    for x in fibo_nums:
        result = '{} {}'.format(result,x)

    print(result)


@app.route('/is-prime', methods=["GET"])
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
