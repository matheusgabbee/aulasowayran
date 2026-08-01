# carrinho_limpo.py

def somar_itens(precos: list[float]) -> float:
    """Recebe dados e devolve o total."""
    return sum(precos)


itens = [10, 20]
total = somar_itens(itens)

print(total)

# entrada explicita, saida explicita
# nenhum estado escondido