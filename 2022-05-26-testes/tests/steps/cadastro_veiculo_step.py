from src.cadastro_veiculo import CadastroVeiculo
from src.veiculo import Veiculo


@given(u'o veiculo com placa "{placa}", identificacao "{id}" e quilometragem "{km}"')
def step_impl(context, placa, id, km):
    context.veiculo = Veiculo(id, placa, km)


@when(u'efetuado o cadastro')
def step_impl(context):
    context.cadastro = CadastroVeiculo()
    context.resultado = context.cadastro.inserir(context.veiculo)


@then(u'o resultado deve ser "Verdadeiro"')
def step_impl(context):
    assert context.resultado == True


@then(u'o veiculo cadastrado deve ter os dados placa "{placa}", identificacao {id} e quilometragem "{km}"')
def step_impl(context, placa, id, km):
    resultado = context.cadastro.consultar(id)

    assert (resultado.placa == placa) and (resultado.km == km)


@given(u'o cadastrado dos dados de veiculos')
def step_impl(context):
    context.cadastro = CadastroVeiculo()
    for dado in context.table:
        veiculo = Veiculo(dado['id'], dado['placa'], dado['km'])
        context.cadastro.inserir(veiculo)


@when(u'o veiculo com id "{id}" for removido')
def step_impl(context, id):
    context.cadastro.remover_por_id(id)


@then(u'a quantidade de veiculos cadastrados deve ser {quantidade}')
def step_impl(context, quantidade):
    resultado = context.cadastro.listar_todos()
    assert len(resultado) == int(quantidade)

@when(u'listado todos os veiculos')
def step_impl(context):
    context.veiculos = context.cadastro.listar_todos()


@then(u'o resultado de ser')
def step_impl(context):
    for row in context.table:
        resultado = list(filter(lambda x: x.id == row['id'], context.veiculos))
        assert resultado[0].placa == row['placa'] and resultado[0].km == row['km']
        