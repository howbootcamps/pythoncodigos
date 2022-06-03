from unittest import TestCase
from src.entities.cliente import Cliente
from src.business.cadastro_cliente import CadastroCliente


class TestCadastroClienteInserir(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cliente = None
        self.cadastro = None

    def setUp(self):
        self.cadastro = CadastroCliente()

    def test_inserir_cliente(self):
        # dado
        cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')

        # quanto
        self.cadastro.inserir(cliente)
        resultado = self.cadastro.listar_todos()

        # entao
        self.assertTrue(resultado[-1].nome == 'Maicon')

    def test_retorno_inserir_cliente(self):
        # dado
        cliente = Cliente('1', 'rua 1', '9988-4433', 'Aluno')

        # quanto
        resultado = self.cadastro.inserir(cliente)

        # entao
        self.assertTrue(resultado == None)

    def test_inserir_quantidade(self):
        # dado
        cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')

        # quanto
        self.cadastro.inserir(cliente)
        resultado = self.cadastro.listar_todos()

        # entao
        self.assertTrue(len(resultado) == 1)