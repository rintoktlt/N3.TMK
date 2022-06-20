import requests

headers = {'Authorization': 'N3 1a55e61b-dd7a-4acf-a94a-37d21d761af5', 'Content-Type': 'application/json', 'Accept': '*/*'}


data = "{'workflowId': '09872eef-6180-4f5f-9137-c33ce60ad416','name': 'test','initialTransitionId': '6ce8ec25-c09b-4bf1-81a9-541f749bac7c','processContext': {}, 'RoleContext': {}}"
url = 'http://r78-test.zdrav.netrika.ru/tm-core/api/Commands/StartNewProcess'
response = requests.post(url, data=data.encode('UTF-8'), headers=headers)
response_dict = response.json()
print(response_dict)
print(response_dict["errorCode"])
print(response.status_code)