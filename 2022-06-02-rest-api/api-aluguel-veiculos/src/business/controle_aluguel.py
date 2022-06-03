
from src.business.aluguel import Aluguel


class ControleAluguel():

    def __init__(self):
        self.__lista: list(Aluguel) = None

    def controle_aluguel(self):
        pass

    def registra_aluguel(self, placa: str):
        pass

    def consulta_aluguel(self, placa: str) -> Aluguel:
        pass

    def listar_alugueis_ativos(self) -> list(Aluguel):
        pass

    def listar_alugueis_concluidos(self) -> list(Aluguel):
        pass

    def listar_todos(self) -> list(Aluguel):
        pass
