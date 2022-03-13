"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Faça um programa que ordene um dicionário por seus valores
"""

dict_to_order = {"matemática": 81, "física": 83, "química": 87}

### Explicação!
# Usei a função `sorted` para ordenar nosso dicionário passando algun argumentos extras
# Link da documentação oficial da função `sorted`: https://docs.python.org/3/library/functions.html#sorted

# dict_to_order.items() -> retorna uma lista de tuplas com chaves e valores de um dicionário: [("matemática", 81), ("física", 83), ("química", 87)]
# O argumento `key` precisa ser uma função (veja na documentação oficial).
# Para esse argumento usei uma função anônima lambda que faz o seguinte: dado uma tupla, retorna o segundo valor dela (índice 1)
# Obs: lembre-se que a indexação começa por zero, então o índice 1 é o segundo valor, que refere-se aos valores do dicionário

# Basicamente o argumento `key` está nos dizendo que devemos ordenar pelos segundos elementos das tuplas de chave-valor!
# Usamos o argumento `reverse=True` para definir a ordem decrescente

# O resultado disso tudo é uma lista de tuplas ordenadas pelo segundo elemento (valor do dicionário)
# [("química", 87), ("física", 83), ("matemática", 81)]

# Por fim, transformamos essa lista de tuplas de volta em um dicionário! o/

ordered_dict = dict(sorted(dict_to_order.items(), key=lambda tupla: tupla[1], reverse=True))

print(ordered_dict)

# PS: esse foi difícil, não foi? =(
# Eu sei, mas estamos aqui para ajudar você a seguir em frente!!
