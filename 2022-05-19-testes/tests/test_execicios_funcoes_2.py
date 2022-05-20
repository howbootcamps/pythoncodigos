from pytest import fixture
from main import reverso

@fixture
def fix():
    print('teste')


def test_reverso(fix):
    # Dados
    valor = 127

    # Quando
    resultado = reverso(valor)

    # Entao
    assert resultado == 721


def test_reverso_array():
    # Dados
    valor = [127, 123, 12141]
    resultado = []
    
    # Quando        
    for i in valor:
        resultado.append(reverso(i))

    # Entao
    valor_retorno = [721, 321, 14121] 

    # Entao
    assert resultado == valor_retorno
