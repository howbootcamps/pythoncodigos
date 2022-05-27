# language: pt

Funcionalidade: Testar a rotina de remoção de veiculos de uma lista 


Cenario: validar a remoção por id
    Dados o cadastrado dos dados de veiculos
    |id | placa     |  km   |
    | 1 |"jtc1988"  |"1231" |
    | 2 |"jtc1988"  |"1231" |
    | 3 |"jtc1988"  |"1231" |
    | 4 |"jtc1988"  |"1231" |
    Quando o veiculo com id "1" for removido
    Entao a quantidade de veiculos cadastrados deve ser 3
    