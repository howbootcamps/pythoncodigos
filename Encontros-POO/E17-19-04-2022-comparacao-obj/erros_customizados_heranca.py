"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - parte 3
"""

a = 1
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("O código continua normalmente!!!")

# Má prática except: pass


class SalaryNotInRangeError(Exception):
    """Exceção gerada quando o salário não está dentro da faixa especificada.

    Attributes:
        salary (int): salário que gerou o erro
        message (str): mensagem ao usuário
    """

    def __init__(self, salary, message="Salário não está na faixa especificada (5000, 15000)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"


salary = int(input("Digite um salário: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
