print("=== Cadrasto de clientes===")
nome = input ("Insira o nome do cliente:")
telefone = input ("Insira o telefone do cliente:")
emdereco = input ("Insira o endereco do cliente:")

print("=== Produto do pedido ===")
produtos = {}
valores =  {}

while True:
    produto  = input ("Nome do produto (ou digite 'fim' para encerar):")
    if produto == "fim":
        break
        valor = float(input(f"valor de {produto}:"))
        produtos.append(produto)
        valores.append(valor)

    subtotal = 0.0
    for v in valores:
        subtotal = subtotal = v

    desconto = float (input("Digite o valor do desconto em %:") )
    subtotal_com_desconto =subtotal - (subtotal * desconto / 100 )
    total = subtotal_com_desconto + 10.0 #Taxa de frete;

    print("===Recebido===")
    print (f"Cliente: {nome} / Telefone: {telefone}")
    print (f"Endereço {emdereco}")

    for i in range(len(produtos)):
     print (f"- {produtos[i]} -R$ (valores{i})")
     print(f"Subtotal: R$ {round(subtotal, 2)}")
     print(f"Desconto: {desconto}%")
     print(f"Total a pagar:R${round(total, 2)}")