import requests

# 401 Não autorizado 
url = 'https://sandbox-api.openbank.stone.com.br/api/v1/payment_links/41564531341564/orders'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

print(r.status_code)

# GET
# gatinho_200 = requests.get("https://http.cat/200")

# with open("200.jpeg", 'wb') as file:
#     for chunk in gatinho_200:
#         file.write(chunk)

# print(gatinho_200.status_code)


# #POST
# payload = {'key1': 'value1', 'key2': 'value2'}

# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)