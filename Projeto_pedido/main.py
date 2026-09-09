from somar_itens import somar_itens
from pedidos import cadastrar_cliente
from pedidos import cadastrar_produtos
from pedidos import calcular_total
from pedidos import emitir_recibo
from somar_itens import somar_itens
from descricao_pedido import descrever_pedido

import pedidos

try:
    cliente = pedidos.cadastrar_cliente()
    produtos = pedidos.cadastrar_produtos()
    valores = [float(v["valor"]) for v in produtos]
    subtotal, total = pedidos.calcular_total(valores)
    pedidos.emitir_recibo(cliente, produtos, subtotal, total)

except:
    print("Error")
