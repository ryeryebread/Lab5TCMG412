from flask import Flask
import hashlib
import math
from itertools import count, islice
import requests
import sys
import getopt

app=Flask('__main__')

@app.route('/is-prime/<num>')
def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


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



@app.route('/fibonacci/<int>')
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

@app.route('/slack-alert/<string>')
def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                            data=payload)
    print(response.text)

    def main(argv):

        message = ''

        try: opts, args = getopt.getopt(argv, "hm:", ["message="])

        except getopt.GetoptError:
            print('SlackMessage.py -m <message>')
            sys.exit(2)
        if len (opts) == 0:
            message = "Hello World"
        for opt, arg in opts:
            if opt == '-h':
                print ('SlackMessage.py -m <message>')
                sys.exit()
            elif opt in ("-m", "--message"):
                message = arg


        send_slack_message(message)

    if __name__ == "__main__":
        main(sys.argv[1:])

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
