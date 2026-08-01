# Conceito:
# Uma closure é uma função interna que "captura" variáveis do escopo
# externo (enclosing) e continua acessando-as mesmo após a função externa terminar.

def criar_desconto(percentual: float):
    """Fábrica de funções de desconto."""

    def aplicar(preco: float) -> float:
        # 'percentual' vem do escopo enclosing
        return preco * (1 - percentual)

    return aplicar


black_friday = criar_desconto(0.30)
cliente_vip = criar_desconto(0.15)

print(black_friday(200))  # 140.0
print(cliente_vip(200))   # 170.0