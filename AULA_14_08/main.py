from cadrastro import normalizar_cpf
try:
     cpf ="125487963312"
     print(normalizar_cpf(cpf))
     
     print(normalizar_cpf(cpf))
except(ValueError, TypeError) as e:
    print("Erro de processamento:", (e))