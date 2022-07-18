import requests
import json
url = "https://hiring.bajajfinservhealth.in/api/renderMe"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

list = json.loads(response.content)
print(list)
