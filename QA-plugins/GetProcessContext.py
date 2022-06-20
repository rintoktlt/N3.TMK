import requests

headers = {'Authorization': 'N3 1a55e61b-dd7a-4acf-a94a-37d21d761af5', 'Content-Type': 'application/json', 'Accept': '*/*'}


data = "{'RoleContext': {},'ProcessId': 'fec15446-4e43-45f7-82e7-9bc843b24521'}"
url = "http://r78-test.zdrav.netrika.ru/tm-core/api/Queries/GetProcessContext"
response = requests.post(url, data=data, headers=headers)
print(response.text)
print(response.status_code)
