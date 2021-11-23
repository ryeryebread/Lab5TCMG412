import sys
import requests

for arg in sys.argv:
    URL = ('http://localhost:5000/' + sys.argv[1] + '/' + sys.argv[2])

    if sys.argv[1] == 'man':
        print ("Enter the url of your request (app *** ***)")
    else:
        result = requests.get(URL)

        results_text = result.json()

        print (results_text)
