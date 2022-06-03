import requests
import json

url = "http://127.0.0.1:5000/cliente"

payload = json.dumps({
  "id": "123332434",
  "endereco": "Rua das flores",
  "telefone": "41 9999-4561",
  "cpf": "350.356.356-45",
  "nome": "Maicon"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
# response = requests.request("GET", url, headers=headers)

print(response.text)
