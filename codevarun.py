import requests

url = "https://hiring.bajajfinservhealth.in/api/renderMe"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
