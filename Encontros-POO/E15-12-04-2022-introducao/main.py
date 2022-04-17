"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - introdução
"""

from pessoas import Funcionario

funcionario1 = Funcionario("João", "Silva", 5000)

funcionario2 = Funcionario("Henrique", "Alves Junqueira Nogueira Branco", 5000)

funcionario3 = Funcionario("Sérgio", "Ramos", 4500)

funcionario1.__salario_inicial = 10000

print(funcionario1.__salario_inicial)
