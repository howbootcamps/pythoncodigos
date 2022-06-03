from src.entities.cliente import Cliente
from src.exceptions.cliente_not_found_error import ClienteNotFoundError
from src.exceptions.not_found_error import NotFoundError
from .cadastro_abstract import CadastroAbtract


class CadastroCliente(CadastroAbtract):
    
    def consultar(self, id: str) -> Cliente:
        try:
            return super().consultar(id)
        except NotFoundError:
            raise ClienteNotFoundError('Cliente não encontrado.')
