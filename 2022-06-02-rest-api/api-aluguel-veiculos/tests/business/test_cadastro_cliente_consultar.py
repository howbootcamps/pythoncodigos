from unittest import TestCase, result
from src.entities.cliente import Cliente
from src.business.cadastro_cliente import CadastroCliente
from src.exceptions.cliente_not_found_error import ClienteNotFoundError


class TestCadastroClienteConsultar(TestCase):

    def test_consulta_cliente_id(self):
        # Dado
        cliente = Cliente('10', 'Rua teste, 550', '99871-2403', 'Monique')
        cadastro = CadastroCliente()

        # Quando
        cadastro.inserir(cliente)
        resultado = cadastro.consultar(cliente.id)

        # Então
        self.assertEqual(resultado.id, '10')

    def test_consulta_cliente_id_especifico(self):
        # Dado
        cliente_a = Cliente('10', 'Rua teste, 550', '99871-2403', 'Monique')
        cliente_b = Cliente('20', 'Rua jose, 50', '99565-2403', 'Matheus')
        cadastro = CadastroCliente()

        # Quando
        cadastro.inserir(cliente_a)
        cadastro.inserir(cliente_b)
        resultado = cadastro.consultar('20')

        # Então
        self.assertEqual(resultado.id, '20')

    def test_consulta_cliente_erro(self):
        # Dado
        cliente_a = Cliente('10', 'Rua teste, 550', '99871-2403', 'Monique')
        cliente_b = Cliente('20', 'Rua jose, 50', '99565-2403', 'Matheus')
        cadastro = CadastroCliente()

        # Quando
        cadastro.inserir(cliente_a)
        cadastro.inserir(cliente_b)

        # Entao
        with self.assertRaises(ClienteNotFoundError):
            cadastro.consultar('40')
