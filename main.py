import requests
import json

headers = {'Authorization': 'N3 1a55e61b-dd7a-4acf-a94a-37d21d761af5'}
data = {
    'workflowId': '09872eef-6180-4f5f-9137-c33ce60ad416',
    'name': 'Тест НСИ',
    'initialTransitionId': '6ce8ec25-c09b-4bf1-81a9-541f749bac7c',
    'processContext': '{}',
    'roleContext': '{}'
}
response = requests.post("http://r78-test.zdrav.netrika.ru/tm-core/api/Commands/StartNewProcess",  headers = headers)
print(response.text)
print(response.status_code)


