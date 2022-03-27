"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""


def inverte_numero(a: int) -> int:
    return int("".join(reversed(str(a))))


print(inverte_numero(127))
