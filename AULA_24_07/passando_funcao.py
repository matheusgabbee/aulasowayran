def gritar (texto):
    return texto.upper() + "!"

def aplicar (funcao, valor):
    return funcao (valor)

print (aplicar(gritar, "python"))