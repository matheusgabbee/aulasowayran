def somar_itens(*valores):
    print(f"Recebi estes valores {valores}")
    return sum (valores)

print(somar_itens(10,30,20,)) #3 valores
print(somar_itens(10,20,))  # 2 valores 
print(somar_itens(1,1,1,1,1)) # 5 valores

