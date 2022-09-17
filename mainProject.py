import sys

import requests
import json

# def runURL1(url):
#     payload = {}
#     headers = {}
#     response = requests.request("GET", url, headers=headers, data=payload)
#     data = json.loads(response.text)
#     company = input("Enter a Company name: ")
#     result = [x for x in data if x["name"] == company]
#     result2 = (result[0]['parks'])
#     print("Here you go...")
#     for x in result2:
#         print(x['name'])
#
# # Compagnie des Alpes


# runURL1("https://queue-times.com/parks.json")

def runURL(url):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)

    print(data['rides'])

runURL("https://queue-times.com/parks/4/queue_times.json")


# Use the ID from the Park API to input into the url for the queue times. Its a string