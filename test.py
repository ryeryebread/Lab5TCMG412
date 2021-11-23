import yaml
import requests

success_total, failed_total = 0

for item in yaml.full_load('test.yaml'):
    ENDPOINT = item['url']
    URL = 'http://localhost:5000' + ENDPOINT
    METHOD = item['method']
    RESULT = item['result']

    if METHOD == 'GET':
        result = requests.get(URL)
    elif METHOD == 'POST':
        result = requests.get(URL + '/' + item[key])
    elif METHOD == 'PUT':
        result = requests.get(URL + '/' + item[key])
    elif METHOD == 'DELETE':
        result = requests.get(URL + '/' + item[key] + '/' + item[string])

        results_text = result.json()

    #need to change to look for status code; results_text is all text rn so wont work
    if results_text == RESULT:
        #success
        success_total += 1

    else: #need to add reasons why failed when adding status codes
        #failed
        failed_total += 1

print("Test passed " + success_total)
print("Test failed " + failed_total)
