"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. 
Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 
"""

# Documentação sobre fatiamento de sequencias: https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html
# Documentação do método .isalpha() de strings: https://docs.python.org/3/library/stdtypes.html#str.isalpha
# Documentação do método .isupper() de strings: https://docs.python.org/3/library/stdtypes.html#str.isupper
# Documentação do método .isdigit() de strings: https://docs.python.org/3/library/stdtypes.html#str.isdigit

placa = input("Digite uma placa: ")

# Validação se a placa tem 8 caracteres (o traço conta!)
if len(placa) != 8:
    placa_valida = False

# Se a placa tiver 8 caracteres, faremos outras validações
else:
    # Aqui separamos apenas as possíveis letras da placa
    possiveis_letras = placa[:3]

    # ... e aqui os possíveis números
    possiveis_numeros = placa[-4:]

    # e até o caracter traço (-)
    traco = placa[3]

    if (
        # Todas as possíveis letras pertencem ao alfabeto? São letras mesmo?
        possiveis_letras.isalpha()
        # ... e estão em maiúscula?
        and possiveis_letras.isupper()
        # ... e os possíveis números são digitos de 0 a 9?
        and possiveis_numeros.isdigit()
        # ... e o traço é mesmo um traço? Poderia ser qualquer outro caracter, não?
        and traco == "-"
    ):
        # Confirmando todas as hipóteses acima, então a placa é válida!
        placa_valida = True

    else:
        # Se alguma das hipóteses não for válida, então a placa inteira náo é válida
        placa_valida = False

print(f"A placa {placa} é válida? Resp: {placa_valida}")
