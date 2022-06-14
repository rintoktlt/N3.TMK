import json
import requests

response = requests.get('http://r78-act.zdrav.netrika.ru/tm-core/api/_version')
obj = json.loads(response.text)
key = "serviceVersion"

if key in obj:
    print(obj['serviceVersion'])
else:
    print (f"Ключа {key} в JSON нет")