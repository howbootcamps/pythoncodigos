from .cliente import Cliente


class PessoaFisica(Cliente):

    def __init__(self, id: str, endereco: str, telefone: str, cpf: str, nome: str):
        super().__init__(id, endereco, telefone, nome)
        self.__cpf = cpf

    @property
    def cpf(self) -> str:
        return self.__cpf
