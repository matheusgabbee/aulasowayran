def conectar (host, porta=5432, timeout=10):
    print (f"{host}: {porta} ({timeout}s)")

    conectar ("localhost")
    conectar ("localhost", 3306)
    conectar ("localhost, timeout=30")