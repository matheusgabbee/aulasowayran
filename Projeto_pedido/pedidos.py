def cadrastrar_clientes():
    nome = input ("Insira o nome do cliente:")
    telefone = input ("Insira o telefone do cliente:")
    endereco = input ("Insira o endereco do cliente:")

    return {"nome":nome, "telefone":telefone, "endereco": endereco}
def cadrastrar_produtos():
    produtos = []

    while True:
        produto  = input ("Nome do produto (ou digite 'fim' para encerar):")
        if produto == "fim":
            break
        valor = float(input(f"valor de {produto}:"))
        produtos.append ({"nome":produto, "valor":valor})
    return produtos

    def calcular_total(valores):  
        subtotal = sum (valores)
        taxa_entrega = 5.0
        total = subtotal + taxa_entrega
        return subtotal, total
    def emitit_recibo(cliente, produtos, subtotal, total):
          print("===Recebido===")
          print(f"Cliente: {cliente['nome']} - {cliente['telefone']}")
          for p in produtos:
              print(f"-{['nome']}: R$ {p['valor']:.2f}")
              print(f"Subtotal:{subtotal:.2f}")  
              print(f"Tatal a pagar :{total:.2f}") 

    clientes = cadrastrar_clientes()
    produtos =cadrastrar_produtos()      
    valores = [p['valor'] for p in produtos]
    subtotal, total = calcular_total(valores)
    emitit_recibo(clientes, produtos,subtotal, total)