
class Veiculo():

    def __init__(self, id, placa, km) -> None:
        self.__id = id
        self.__placa = placa
        self.__km = km

    @property
    def id(self):
        return self.__id


    @property
    def placa(self):
        return self.__placa

    @property
    def km(self):
        return self.__km