from src.entities.veiculo import Veiculo


class Automovel(Veiculo):

    def __init__(self, id: str, placa: str, km: float, bagageiro: int, portas: int):
        super().__init__(id, placa, km)
        self.__bagageiro = bagageiro
        self.__portas = portas

    @property
    def bagageiro(self) -> int:
        return self.__bagageiro

    @property
    def portas(self) -> int:
        return self.__portas
