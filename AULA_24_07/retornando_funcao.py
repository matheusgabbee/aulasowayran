def multiplicador (fator):
    def multiplicar (n):
        return n * fator

    return multiplicar 

dobro = multiplicador (2)
print (dobro(5))
