import re

"""O comando dentro da função dessa biblioteca python 're.sub' ignora os caracteres,
mantendo apenas os números."""
def normalizar_cpf(cpf: str) -> str:
    if not cpf == str:
        tipo = type(cpf)
        raise TypeError("Erro de tipo: O tipo informado de CPF não corresponde com o esperado pela função. Tipo esperado = str, informado: <class 'int'>")
    return re.sub(r"\D", "", cpf)
    
"""Essa função está validando se o cpf é válido usando o 'and' para verificar se a entrada 
possui 11 dígitos e se todos os dígitos são de fato dígitos (e não caracteres).
O 'and' precisa ser usado pois se trata de uma verificação dupla (11 dígitos e e sem caracteres)"""
def validar_cpf(cpf: str) -> bool:
    if not isinstance(cpf, str):
        tipo = type(cpf)
        raise TypeError("Erro de tipo: O tipo informado de CPF não corresponde com o esperado pela função. Tipo esperado = str, informado: <class 'int'>")
    return len(cpf) == 11 and cpf.isdigit() 

"""Essa função recebe a primeira função 'normalizar' e a segunda 'validar'.
Se o resultado da segunda função for 'false' ela irá retornar um ValueError com a mensagem 'CPF inválido'."""
def cadastrar_cliente(cpf: str):
    cpf = normalizar_cpf(cpf)

    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")
    return salvar_cliente(cpf)