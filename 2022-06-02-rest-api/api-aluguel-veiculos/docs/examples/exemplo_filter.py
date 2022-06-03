from traceback import print_list
from src.business.cadastro_cliente import CadastroCliente
from src.entities.cliente import Cliente
from src.entities.entity import Entity
from src.entities.pessoa_fisica import PessoaFisica
from src.entities.pessoal_juridica import PessoaJuridica


cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')


cliente_pessoa_fisica = PessoaFisica(
    '2', 'rua 2', '9999-5555', '542.521.532-85', 'Henrique')
cliente_pessoa_juridica = PessoaJuridica(
    '3', 'rua 3', '9999-7777', '12.169.185/0001-42', 'Henrique LTDA')

lista_clientes = []

lista_clientes.append(cliente)
lista_clientes.append(cliente_pessoa_fisica)
lista_clientes.append(cliente_pessoa_juridica)

lista_filtrada = []

# 1
# for cliente in lista_clientes:
#     if cliente.id == '3':
#         lista_filtrada.append(cliente)

# 2
# def valida_id(cliente, id):
#     resultado = cliente.id == id
#     return resultado

# for cliente in lista_clientes:
#     if valida_id(cliente, '3'):
#         lista_filtrada.append(cliente)

# 3
# funcao = lambda cliente: cliente.id == '3'
# lista_filtrada = list(filter(funcao, lista_clientes))

# 4
id = '3'
lista_filtrada = list(filter(lambda cliente: cliente.id == id, lista_clientes))


print(lista_filtrada[0].nome)