"""
How Bootcamps - Stone - /código[s]
Data: 14/04/2022
Autor: Henrique Junqueira Branco
Enunciado: Exemplo simples sobre herança e polimorfismo
"""
# Classe mãe Ave
class Ave:
    def __init__(self, numero_de_patas, cor, tamanho):
        self.numero_de_patas = numero_de_patas
        self.cor = cor
        self.tamanho = tamanho

    def voar(self):
        print("Ave voando!")


# Subclasse de Ave: herança!
class Tucano(Ave):
    def __init__(self, machando_no_olho):

        # Iniciando os atributos da classe mãe
        super().__init__(self, 2, "colorido", "pequeno porte")

        # Atributi específico da classe Tucano
        self.tem_machando_no_olho = machando_no_olho

    # Sobrescrevendo o método da classe mãe: polimorfismo!
    def voar(self):
        print("Voando como um tucano!")


# Criando um objeto da classe Ave
ave_generica = Ave(2, "preta", "grande porte")

# Criando um objeto da classe Tucano
tucano1 = Tucano(True)

# Método `voar`do objeto ave_generica do tipo Ave
ave_generica.voar()

# Método `voar` do objeto tucano1 da classe Tucano
tucano1.voar()

# Atributo `tem_machando_no_olho` do objeto tucano1 da classe Tucano
print(tucano1.tem_machando_no_olho)
