import requests

response = requests.get('http://r78-act.zdrav.netrika.ru/tm-core/api/_version')
print (response.text)