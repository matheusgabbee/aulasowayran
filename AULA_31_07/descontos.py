def calcular_desconto(
    valor: float,
    percentual: float,
) -> float:

    return round(valor * (1 - percentual), 2)