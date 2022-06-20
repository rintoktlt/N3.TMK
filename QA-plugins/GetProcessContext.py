import requests

headers = {'Authorization': 'N3 1a55e61b-dd7a-4acf-a94a-37d21d761af5', 'Content-Type': 'application/json', 'Accept': '*/*'}


data = "{'RoleContext': {},'ProcessId': '4978798e-296b-4c20-a5ba-4c15f09b5d13'}"
url ="http://r78-test.zdrav.netrika.ru/tm-core/api/Queries/GetProcessContext"
response = requests.post(url, data=data, headers=headers)
print(response.text)
print(response.status_code)
