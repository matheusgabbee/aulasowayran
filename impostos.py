def calcular_imposto(valor, aliquota):
    """Só usa os argumentos."""
    return round(valor * aliquota, 2)

calcular_imposto(100, 0.18)
# 18.0

# Sempre o mesmo resultado para os mesmos argumentos.