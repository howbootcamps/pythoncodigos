from src.veiculo import Veiculo
from src.cadastro_veiculo import CadastroVeiculo


def test_retorno_inserir():
    # Dado
    veiculo = Veiculo('123', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando
    resultado = cadastro.inserir(veiculo)

    # Entao
    assert resultado


def test_consultar_veiculo_cadastrado_por_id():
    # Dado
    veiculo = Veiculo('123', 'rere', 'erer')
    cadastro = CadastroVeiculo()

    # Quando
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('123')

    # Entao
    assert resultado.id == '123'


def test_consultar_id_veiculo_inserido():
    # Dado
    veiculo = Veiculo('1321', 'gol', 1263456)
    cadastro = CadastroVeiculo()

    # Quando
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1321')

    # Entao
    assert resultado.id == '1321'


def test_consultar_km_veiculo_inserido():
    # Dado
    veiculo = Veiculo('1321', 'gol', 1263456)
    cadastro = CadastroVeiculo()

    # Quando
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1321')

    # Entao
    assert resultado.km == 1263456


def test_consultar_placa_veiculo_inserido():
    # Dado
    veiculo = Veiculo('1321', 'gol', 1263456)
    cadastro = CadastroVeiculo()

    # Quando
    cadastro.inserir(veiculo)
    resultado = cadastro.consultar('1321')

    # Entao
    assert resultado.placa == 'gol'


def test_remover_por_id_veiculo():
    # Dado
    veiculo = Veiculo('1321', 'gol', 1263456)
    cadastro = CadastroVeiculo()

    # Quando
    cadastro.inserir(veiculo)
    resultado = cadastro.remover_por_id('1321')

    # Entao
    assert resultado

def test_validar_remocao():
    # Dado
    veiculo_a = Veiculo('1321', 'gol', 1263456)
    cadastro = CadastroVeiculo()

    # Quando
    cadastro.inserir(veiculo_a) 
    cadastro.remover_por_id('1321')

    resultado = cadastro.consultar('1321')

    # Entao
    assert resultado is None