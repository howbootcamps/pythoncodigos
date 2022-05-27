# language: pt

Funcionalidade: teste de cadastro de veiculos inserir


Cenario: validar o retorno do metodo inserir veiculo
    Dado o veiculo com placa "jtc1988", identificacao "123" e quilometragem "123546"
    Quando efetuado o cadastro 
    Entao o resultado deve ser "Verdadeiro"

Cenario: validar o retorno do metodo inserir veiculos
    Dado o veiculo com placa "teste", identificacao "45645" e quilometragem "464564"
    Quando efetuado o cadastro 
    Entao o veiculo cadastrado deve ter os dados placa "teste", identificacao 45645 e quilometragem "464564"

Cenario: validar veiculos cadastrados
    Dados o cadastrado dos dados de veiculos
    |id | placa     |  km   |
    | 1 |"jtc1988"  |"1231" |
    | 2 |"jtc1988"  |"1231" |
    | 3 |"jtc1988"  |"1231" |
    | 4 |"jtc1988"  |"1231" |
    Quando listado todos os veiculos
    Entao o resultado de ser
    |id | placa     |  km   |
    | 1 |"jtc1988"  |"1231" |
    | 2 |"jtc1988"  |"1231" |
    | 3 |"jtc1988"  |"1231" |
    | 4 |"jtc1988"  |"1231" |
