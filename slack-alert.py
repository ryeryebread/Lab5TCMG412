import requests
import sys
import getopt

def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                            data=payload)
    print(response.text)

def main(argv):

    message = ''

    try: opts, args = getopt.getopt(slackalert, "hm:", ["message="])

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