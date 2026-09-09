def cadrastrar_Cliente():
    nome = input ("insira seu nome")
    telefone = input("insira seu numero")
    return nome , telefone

def cadrartarProdutos():
    produtos = {}
    while True:
        nomedeProduto =input("insira o nome do produto ou pare:")
        if nomedeProduto =="pare":
            break
        valordeProduto = float(input("insira o valor do produto:"))

        produtos.append ({"nome":nomedeProduto, "valor":valordeProduto})
        produtos ={"nome": nomedeProduto, "preco": valordeProduto}
        produtos.append(produtos)
    return produtos