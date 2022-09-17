import requests

url = "https://queue-times.com/parks.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)