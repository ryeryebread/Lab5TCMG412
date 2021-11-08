from flask import Flask, request, jsonify, render_template
import hashlib
from math import sqrt
import math
from itertools import count, islice
import requests
import sys
import getopt
import redis


#PORT MAY BE WRONG
r = redis.Redis(host='redis', port=5000, db=0)



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
def fibo_sec(n):
    if n ==0 or n is None :
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        #do fibonacci
        return fibo_sec(n-2) + fibo_sec(n-1)



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



#LAB 6
#GET FUNCTION
@FLASK_APP.route("/keyval/<string:key_string>", methods=["GET"])
def get_value(key_string):
    try:
        temp_string = r.get(key_string)
    except redis.RedisError:
        return jsonify(key=key_string,
                        value=False,
                        command="GET " + key_string,
                        result=False,
                        error="Key does not exist."), 400


    if redis.Redis.exists(key_string) == False:
        return jsonify(key=key_string,
                        value=False,
                        command="GET " + key_string,
                        result=False,
                        error="Key does not exist."), 404

    else:
        val = redis.REDIS.get(key_string)
        return jsonify(key=key_string,
                        value=val,
                        command="GET " + key_string,
                        result=True,
                        error=""), 200