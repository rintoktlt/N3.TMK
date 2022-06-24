import json
import requests
import pytest

headers = {'Authorization': 'N3 1a55e61b-dd7a-4acf-a94a-37d21d761af5', 'Content-Type': 'application/json', 'Accept': '*/*'}
url = 'http://r78-test.zdrav.netrika.ru/tm-core/api/Commands/StartNewProcess'
workflowId = '09872eef-6180-4f5f-9137-c33ce60ad416'
name = 'RIV-test'
initialTransitionId = '6ce8ec25-c09b-4bf1-81a9-541f749bac7c'
processContext = '"lpu": {"idLpu": "d56b1535-6691-4db7-b10e-70a983b841ec"}'

class TestNSI:
    def test_nsi_in_object(self):
        data = "{'workflowId': '"+workflowId+"','name': '"+name+"','initialTransitionId': '"+initialTransitionId+"','processContext': {"+processContext+"}, 'RoleContext': {}}"
        response = requests.post(url, data=data.encode('UTF-8'), headers=headers)
        assert response.status_code == 200
        response_dict = response.json()
        assert response_dict["errorCode"] == 0, "Value errorCode<>0"
