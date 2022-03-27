"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Escreva uma função que, dado três comprimentos de retas quaisquer, diga se essas três retas podem ou não formar um triângulo, retornando true em caso positivo e false em caso negativo.

Dica n°1: Se algum dos comprimentos for negativo ou zero, não é possível formar um triângulo.
Dica n°2: se qualquer um dos comprimentos for maior ou igual à soma dos outros dois, então os comprimentos não podem ser usados para formar um triângulo. 
Caso contrário, eles podem formar um triângulo.
"""


def forma_triangulo(a: int, b: int, c: int) -> bool:

    zerados_ou_negativos = a <= 0 or b <= 0 or c <= 0

    lado_maior_que_soma_dos_outros = a > b + c or b > a + c or c > a + b

    if zerados_ou_negativos or lado_maior_que_soma_dos_outros:
        return False

    return True


print(f"É possível formar um triângulo com os lados 3, 4 e 5? Resp: {forma_triangulo(3,4,5)}")
print(f"É possível formar um triângulo com os lados 1, 1 e 10? Resp: {forma_triangulo(1,1,10)}")
print(f"É possível formar um triângulo com os lados 0, 4 e 5? Resp: {forma_triangulo(0,4,5)}")
