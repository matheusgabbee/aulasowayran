class CPFInvalido(Exception):
    pass
def validar_cpf(cpf: str) -> bool:
    return True
def calcular_total(itens) -> float:
    return 0.0
def calcular_imposto(total: float) -> float:
    return 0.0
def salvar_pedido(pedido) -> int:
    return 1
def processar_pedido(dados):
    if not validar_cpf(dados.cpf):
        raise CPFInvalido()
    total = calcular_total(dados.itens)
    total += calcular_imposto(total)

    return salvar_pedido(dados)