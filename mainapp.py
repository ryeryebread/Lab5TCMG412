
from flask import Flask, request, jsonify
import hashlib
from math import sqrt
from itertools import count, islice
import requests
import sys
import getopt
from redis import Redis,StrictRedis,RedisError


#Use strict redis
redis = StrictRedis('redis', 6379, charset="utf-8", decode_responses=True)
app = Flask(__name__)


# I REPLACED ALL OF FACTORIAL; this should work now
@app.route('/factorial/<int:a>')
def factorial(num):
    temp_num = 1
    if num < 0:
        return jsonify(
            input=int(num),
            output="Error: Input not positive"
        )

    elif num == 0:
        return jsonify(
            input=int(num),
            output=int(1)
        )

    else:
        for i in range(1, num):
            temp_num = temp_num * i
        return jsonify(
            input=int(num),
            output=int(factorial)
        )


@app.route('/fibonacci/<int:start_num>')
def fib(x):
    return jsonify(
        input=x,
        output=fibo_sec(x)
    )


# NEED TO FIX ASKING FOR INPUT AND ADD RETURN
def fibo_sec(n):
    if n == 0 or n is None:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        # do fibonacci
        return fibo_sec(n - 2) + fibo_sec(n - 1)


@app.route('/is-prime/<int:n>')
def prime(x):
    return jsonify(
        input=x,
        output=is_prime(x)
    )


# THIS MIGHT WORK; need to test
def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

    # We dont need this code right?
    for i in range(1, 500):
        if is_prime(i) == True:
            print(i, end=' ')


@app.route('/md5/<string:result>')
def md5(string):
    # not sure this works. just inferred from what was already here
    result = string
    result = hashlib.md5(string.encode())
    result = result.hexdigest()

    return jsonify(
        input=string,
        output=result)


# Slack alert
@app.route('/slack-alert/<string:message>')
def slackalert(message):
    payload = '{"text":"%s"}' % message
    requests.post('https://hooks.slack.com/services/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', data=payload)
    return jsonify(input=message, output=True)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')


# LAB 6


# POST function
@app.route('/keyval', methods=['POST'])
def handle_post():
    client_data = request.get_json()
    v = client_data('value')

    # Check for valid JSON
    if client_data.get('key'):
        k = client_data.get('key')
    else:
        k = ''
        err_string = "Invalid request from client"
        return jsonify(
            key=k,
            value=v,
            command=f"CREATE {k}/{v}",
            result=False,
            error=err_string
        ), 400

    # Check if key already exists
    if redis.exists(k):
        err_string = "Key already exists"
        return jsonify(
            key=k,
            value=v,
            command=f"CREATE {k}/{v}",
            result=False,
            error=err_string
        ), 409

    # Store data in redis
    redis_result = redis.set(k, v)
    if redis_result == False:
        err_string = "Could not write to DB"
    else:
        err_string = None

    return jsonify(
        key=k,
        value=v,
        command=f"CREATE {k}/{v}",
        result=redis_result,
        error=err_string
    ), 400


# PUT function
@app.route('/keyval', methods=['PUT'])
def handle_put():
    client_data = request.get_json()
    v = client_data('value')

    # Check for valid JSON
    if client_data.get('key'):
        k = client_data.get('key')
    else:
        k = ''
        err_string = "Invalid request from client"
        return jsonify(
            key=k,
            value=v,
            command=f"CREATE {k}/{v}",
            result=False,
            error=err_string
        ), 400

    # Check if key doesn't exist
    if redis.exists(k):
        err_string = "Key already exists"
        return jsonify(
            key=k,
            value=v,
            command=f"CREATE {k}/{v}",
            result=False,
            error=err_string
        ), 409
    else:
        # store data in redis
        redis_result = redis.set(k, v)
        if redis_result == False:
            err_string = "Could not write to DB"
        else:
            err_string = None
            return jsonify(
                key=k,
                value=v,
                command=f"CREATE {k}/{v}",
                result=redis_result,
                error=err_string
            )


# GET FUNCTION
@app.route("/keyval/<string:key_string>", methods=["GET"])
def get_value(key_string):
    try:
        temp_string = redis.get(key_string)
    except redis.RedisError:
        return jsonify(key=key_string,
                       value=False,
                       command="GET " + key_string,
                       result=False,
                       error="Invalid request"), 400

    if redis.Redis.exists(key_string) == False:
        return jsonify(key=key_string,
                       value=temp_string,
                       command="GET " + key_string,
                       result=False,
                       error="Key does not exist."), 404

    else:
        val = redis.Redis.get(key_string)
        return jsonify(key=key_string,
                       value=val,
                       command="GET " + key_string,
                       result=True,
                       error=""), 200


# DELETE function
@app.route("/keyval/<string:key_string>", methods=["DELETE"])
def delete(key_string):
    try:
        temp_string = redis.get(key_string)
    except Redis.RedisError:
        return jsonify(key=key_string,
                       value=False,
                       command="DELETE " + key_string,
                       result=False,
                       error="Invalid request"), 400

    if redis.Redis.EXISTS(key_string):
        redis.Redis.delete(key_string)
        return jsonify(key=key_string,
                       value=temp_string,
                       command="DELETE " + key_string,
                       result=True,
                       error=""), 200
    else:
        return jsonify(key=key_string,
                       value=temp_string,
                       command="DELETE " + key_string,
                       result=False,
                       error="Key does not exist."), 404


#{
#    "success": True,
#    "string": "user updated with ID 4",
#    "id": 4
#}
#
#{
#    "message": "Invalid Application-Id or API-Key"
#}