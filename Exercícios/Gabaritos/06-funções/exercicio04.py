"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Embaralha palavras: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

from random import shuffle


def embaralha_string(str_input: str) -> str:
    str_list = [letra.upper() for letra in str_input]
    shuffle(str_list)
    return "".join(str_list)


print(embaralha_string("Python"))
