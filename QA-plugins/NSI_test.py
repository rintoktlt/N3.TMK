import json
import requests
import pytest

class TestNSI:
    def test_NSI_in_object(self):
        data={'workflowId': '09872eef-6180-4f5f-9137-c33ce60ad416',
              'name': 'Тест НСИ',
              'initialTransitionId': '6ce8ec25-c09b-4bf1-81a9-541f749bac7c',
              'processContext': '{},',
              'roleContext': '{}'
              }
        response = requests.post('http://r78-test.zdrav.netrika.ru/tm-core/api/Commands/StartNewProcess', data=data)
        print ()
        assert "humanFriendlyId2"
