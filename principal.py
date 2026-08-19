from numeros import generar_turno

perfumeria = generar_turno("P")
farmacia = generar_turno("F")
cosmetica = generar_turno("C")

areas = {
    "1": (perfumeria, "Perfumeria"),
    "2": (farmacia, "Farmacia"),
    "3": (cosmetica, "Cosmetica"),
}


def menu():
    while True:
        print("""
    =*=*=*=*=*=*=*=*=*=*=*=*=*
    TURNERO DE FARMACIA
    =*=*=*=*=*=*=*=*=*=*=*=*=*
    [1] - Perfumeria
    [2] - Farmacia
    [3] - Cosmetica
    =*=*=*=*=*=*=*=*=*=*=*=*=*
        """)
        opcion = input("A que area se dirije?: ")
        if opcion not in areas:
            print("Opcion invalida, intenta de nuevo.")
            continue
        generador, nombre = areas[opcion]
        numero = next(generador)
        print(f"Area: {nombre}")
        print(f"Este es tu ticket: {numero}")
        print("Espere y sera atendido")
        while True:
            respuesta = input("Otro turno?: ").lower()
            if respuesta in ["si", "s", "yes", "y"]:
                break
            elif respuesta in ["no", "n"]:
                print("Gracias por usar el turnero. Hasta luego.")
                return
            else:
                print("Responde si o no.")


menu()
