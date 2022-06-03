from .entity import Entity


class Cliente(Entity):

    def __init__(self, id: str, endereco: str, telefone: str, nome: str):
        super().__init__(id)
        self.__endereco: str = endereco
        self.__telefone: str = telefone
        self.__nome: str = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @property
    def telefone(self) -> str:
        return self.__telefone

    @property
    def nome(self) -> str:
        return self.__nome
