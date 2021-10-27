from flask import Flask, jsonify
import hashlib
import math
from itertools import count, islice


app=Flask('__main__')

@app.route('/is-prime/<num>')
def prine(x):
    return jsonify(
        input=x,
        output=is_prime(x)
    )


def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

#Do we need this?
for i in range(1, 500):

    if is_prime(i) == True:
        print(i, end=' ')


@app.route("/factorial/<num>")
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

    print(str('You can choose'), a, str('objects from'), b, str('objects in'), my_combinations(a, b), str('ways'))


factorial()


@app.route('/fibonacci/<int>')
def fib(x):
    return jsonify(
        input = x,
        output = fibo_sec(x)
    )

#NEED TO CHANGE FOR JUST ONE INPUT
def fibo_sec(n):
    if n <=0:
        #NEED TO RETURN AN ERROR
        print()


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

        if (first_fibo > end_num):
            break

    print('\nThe {} Fibonacci numbers between {} and {} are:'.format(len(fibo_nums), start_num, end_num))
    result = ''
    for x in fibo_nums:
        result = '{} {}'.format(result, x)

    print(result)


fibo_sec()


@app.route("/factorial/<int>")
def factorial(num):
    temp_num = 1
    if num < 0:
        return jsonify(
			input = int(num),
			output = "Error: Input not positive"
            )
    
    elif num == 0:
        return jsonify(
			input = int(num),
			output = int(1)
            )

    else:
        for i in range(1,num):
            temp_num = temp_num*i
        return jsonify(
			input = int(num),
			output = int(factorial)
            )




if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
    
    
    
    
    
    
    
    
    

