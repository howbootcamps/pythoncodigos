from src.business.cadastro_cliente import CadastroCliente
from src.entities.cliente import Cliente
from src.entities.pessoa_fisica import PessoaFisica
from src.entities.pessoal_juridica import PessoaJuridica
from src.exceptions.base_aluguel_error import BaseAluguelError


cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')

cliente_pessoa_fisica = PessoaFisica(
    '2', 'rua 2', '9999-5555', '542.521.532-85', 'Henrique')
cliente_pessoa_juridica = PessoaJuridica(
    '3', 'rua 3', '9999-7777', '12.169.185/0001-42', 'Henrique LTDA')


cadastro = CadastroCliente()

cadastro.inserir(cliente)
cadastro.inserir(cliente_pessoa_fisica)
cadastro.inserir(cliente_pessoa_juridica)

try:
    pessoa_juridica = cadastro.consultar('3')
    print(pessoa_juridica.nome)

    pessoa_anonima = cadastro.consultar('2')
    print(pessoa_anonima.nome)

    cadastro.remover_por_id('1')

    cadastro.remover_por_id('5')

    todos_clientes = cadastro.listar_todos()

    # print(todos_clientes)

    cadastro.remover_por_entidade(cliente_pessoa_juridica)

    todos_clientes = cadastro.listar_todos()
except BaseAluguelError as ex:
    print(f"DEU O ERRO, {ex.mensagem}")




print('FIM')
