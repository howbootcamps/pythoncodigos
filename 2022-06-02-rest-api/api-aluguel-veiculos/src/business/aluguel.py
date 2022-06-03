from datetime import datetime
from src.entities.cliente import Cliente
from src.entities.veiculo import Veiculo


class Aluguel():

    def __init__(self):
        self.cliente: Cliente = None
        self.veiculo: Veiculo = None
        self.ativo: bool = True
        self.data_retirada: datetime = datetime.now()
        self.data_devolucao: datetime = datetime.now()
        self.valor_diaria: float = None
        self.valor_apagar: float = None

    def aluguel(self, cliente: Cliente, veiculo: Veiculo, valor_diaria: float):
        pass

    def devolucao(self):
        pass

    def calcular_valor_apagar(self, cliente: Cliente, veiculo: Veiculo) -> float:
        pass
