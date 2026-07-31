def processar_pedido(dados):
    if not dados["cpf"]:
        return False 
    total = 0
    for i in dados["itens"]:
        total += i["preco"] * i["qtd"]
    imposto = total * 0.18  # regra fixa
    db.execute("INSERT ...")  # acesso direto
    smtp.send(dados["email"])  # efeito
    print("ok")
    return total + imposto