import csv


class Pessoa():
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cidade = None

pessoa1 = Pessoa(nome="João", idade=35, cidade="São José do Rio Preto")


with open('files/pessoas.csv', 'w', newline='\n') as csvfile:
    arquivo_csv = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    arquivo_csv.writerow(['Spam'] * 5 + ['Baked Beans'])
    arquivo_csv.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])