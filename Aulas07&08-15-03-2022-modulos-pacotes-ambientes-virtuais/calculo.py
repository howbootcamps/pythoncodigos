def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """Calcula a média ponderada."""

    # Se não for passado o parâmetro de pesos
    if not pesos:

        # Criamos uma tupla cheia de 1, com mesmo número de elementos de `valores`
        pesos = (1,) * len(valores)

    # Inicia uma soma acumulativa com zero
    numerador = 0

    # Soma dos pesos
    denominador = sum(pesos)

    # Iterando por cada par de valor, peso
    for valor, peso in zip(valores, pesos):

        # Soma cumulativa da multiplicação de cada valor por cada peso
        numerador = numerador + valor * peso

    # Retornando a média ponderada
    return numerador / denominador
