import pytest
from src.veiculo import Veiculo


def test_inserir_set_placa_veiculo_error():
    # Dado
    veiculo = Veiculo('123', 'rere', 'erer')

    # Quando
    # Entao
    with pytest.raises(AttributeError):
        veiculo.placa = 'teste'


def test_inserir_set_id_veiculo_error():
    # Dado
    veiculo = Veiculo('123', 'rere', 'erer')

    # Quando
    # Entao
    with pytest.raises(AttributeError):
        veiculo.id = 'teste'


def test_inserir_set_km_veiculo_error():
    # Dado
    veiculo = Veiculo('123', 'rere', 'erer')

    # Quando
    # Entao
    with pytest.raises(AttributeError):
        veiculo.km = 'teste'
