import requests
import json

def runURL1(url):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    print("Company name is = " + data[0]['name'])
    print("Park name is = " + data[0]['parks'][0]['name'])


runURL1("https://queue-times.com/parks.json")

# def runURL(url):
#     payload = {}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     data = json.loads(response.text)
#     print("Wait time = " + str(data['rides'][0]['wait_time']))
#
# runURL("https://queue-times.com/parks/2/queue_times.json")
