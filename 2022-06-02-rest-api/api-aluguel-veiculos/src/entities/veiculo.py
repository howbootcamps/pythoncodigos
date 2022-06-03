from src.entities.entity import Entity


class Veiculo(Entity):

    def __init__(self, id: str, placa: str, km: float):
        super().__init__(id)
        self.__placa = placa
        self.__km = km

    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def km(self) -> float:
        return self.__km
