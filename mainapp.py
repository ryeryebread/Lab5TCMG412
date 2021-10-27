from flask import Flask, request, jsonify, render_template
import hashlib
from math import sqrt
import math
from itertools import count, islice
import requests
import sys
import getopt


app = Flask(__name__)


#I REPLACED ALL OF FACTORIAL; this should work now
@app.route('/factorial/<int:a>', methods=["GET"])
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


@app.route('/fibonacci/<int:start_num>', methods=["GET"])
def fib(x):
    return jsonify(
        input = x,
        output = fibo_sec(x)
    )

#NEED TO FIX ASKING FOR INPUT AND ADD RETURN
def fibo_sec():
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



@app.route('/is-prime/<int:n>', methods=["GET"])
def prime(x):
    return jsonify(
        input=x,
        output=is_prime(x)
    )

#THIS MIGHT WORK; need to test
def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

    #We dont need this code right?
    for i in range (1, 500):

        if is_prime(i)==True:

            print(i,end=' ')

@app.route('/md5/<string:result>', methods=["GET"])
def md5(string):
    #not sure this works. just inferred from what was already here
    result = string
    result = hashlib.md5(string.encode())
    result = result.hexdigest()

    return jsonify(
		input = string,
		output =result)



@app.route('/slack-alert/<string:message>')
def slackalert(message):
    payload = '{"text":"%s"}' % message
    requests.post('https://hooks.slack.com/services/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',data=payload)
    return('ok')
    
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
