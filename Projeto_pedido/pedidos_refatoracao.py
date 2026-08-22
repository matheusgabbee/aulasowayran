def     calcular_total (valores, desconto=0.0, taxa_entrega=10.0):
        subtotal = sum(valores)
        subtotal_com_desconto = subtotal - (subtotal * desconto / 100)
        total = subtotal_com_desconto + taxa_entrega
        return subtotal, total

desconto = float(input("Digite o valor do desconto em %:") )
taxa_entrega = float(input("Digite o valor da taxa de entrega: "))
total = calcular_total (valores= [10, 10 ,10, 10], taxa_entrega=taxa_entrega, desconto=desconto)
print(total)
