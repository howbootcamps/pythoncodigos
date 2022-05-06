import json

class Veiculo():
    def __init__(self):
        self.marca = None
        self.modelo = None

    def salvar(self):
        print("teste")
    

class Pessoa():
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cidade = None
        self.veiculos: list = []

fusca = Veiculo()
fusca.marca = "VW"
fusca.modelo = "fusca"

chevete = Veiculo()
chevete.marca = "GM"
chevete.modelo = "chevete"

chevete.salvar()


maicon = Pessoa()
maicon.nome = 'Maicon'
maicon.idade = 35
maicon.cidade = 'Curitiba'
maicon.veiculos.append(fusca.__dict__)
maicon.veiculos.append(chevete.__dict__)


maicon_json = json.dumps(maicon.__dict__)


with open('files/maicon.json', 'rb') as arquivo:
    teste = arquivo.read()

# with open('files/maicon.json', 'r') as arquivo:
#     lista_de_maicons = arquivo.read()

# lista = json.loads(lista_de_maicons)

print("FIM")
        


# {
#     "en": "English",     
#     "es": "Spanish", 
#     "fr": "French", 
#     "ja": "Japanese", 
#     "ko": "Korean", 
#     "pt-br": "Brazilian Portuguese", 
#     "zh-cn": "Simplified Chinese", 
#     "zh-tw": "Traditional Chinese"
# }


# maicon = '{"nome": "maicon","idade": 35,"cidade": "curitiba"}'

# print(maicon)


# objeto_maicon = json.loads(maicon)

# print(objeto_maicon)
