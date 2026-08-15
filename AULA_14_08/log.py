def log_execucao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("início: %s", func.__name__)
        resultado = func(*args, **kwargs)
        logger.info("fim: %s", func.__name__)
        return resultado
    return wrapper           #closure: lembra func

@log_execucao
def processar_pedido(pedido: Pedido) -> Recibo:
    ...