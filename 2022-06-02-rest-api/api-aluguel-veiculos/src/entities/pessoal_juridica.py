from .cliente import Cliente


class PessoaJuridica(Cliente):

    def __init__(self, id: str, endereco: str, telefone: str, cnpj: str, nome: str):
        super().__init__(id, endereco, telefone, nome)
        self.__cnpj = cnpj

    @property
    def cnpj(self) -> str:
        return self.__cnpj
