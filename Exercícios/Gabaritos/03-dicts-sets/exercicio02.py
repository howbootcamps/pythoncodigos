"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado.
"""

estado_sigla = {
    "RR": "Roraima",
    "AP": "Amapá",
    "AM": "Amazonas",
    "PA": "Pará",
    "AC": "Acre",
    "RO": "Rondônia",
    "TO": "Tocantins",
    "MA": "Maranhão",
    "PI": "Piauí",
    "CE": "Ceará",
    "RN": "Rio Grande do Norte",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "AL": "Alagoas",
    "SE": "Sergipe",
    "BA": "Bahia",
    "MT": "Mato Grosso",
    "DF": "Distrito Federal",
    "GO": "Goiás",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "ES": "Espírito Santo",
    "RJ": "Rio de Janeiro",
    "SP": "São Paulo",
    "PR": "Paraná",
    "SC": "Santa Catarina",
    "RS": "Rio Grande do sul",
}

sigla = input("Digite uma sigla: ")

if sigla in estado_sigla:
    print(f"O nome completo do estado é {estado_sigla[sigla]}")
else:
    print("Sigla inválida!")
