import requests

response = requests.get('http://r78-act.zdrav.netrika.ru/tm-core/api/_version')
parsed_response_text = response.json()

print(f"Полный ответ от сервиса")
print(parsed_response_text)
print(f"----")
print(f"Запрашиваем значение serviceVersion")
print(parsed_response_text["serviceVersion"])
print(f"----")
print(f"Запрашиваем Код ответа")
print(response.status_code)