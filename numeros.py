def generar_turno(prefijo, inicial=1):
    numero = inicial
    while True:
        yield f"{prefijo}-{numero}"
        numero += 1
