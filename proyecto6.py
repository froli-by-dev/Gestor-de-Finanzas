from pathlib import Path
import os
#instrucciones basicas
def prints():
    print("=*=*=*=*=*=*=*=*=*")
    print("Programa: Organizador recetas")
    print("=*=*=*=*=*=*=*=*=*")
def ruta_recetas():
    ruta = Path("recetas").absolute()
    return ruta
def cantidad_recetas():
    ruta = Path(__file__).parent.parent / "recetas"
    cantidad = len(list(ruta.rglob("*.txt")))
    return cantidad
cantidad_recets= cantidad_recetas()
rutas= ruta_recetas()
def leer_receta():
    ruta = Path(__file__).parent.parent / "recetas"
    while True:
        os.system("clear")
        categorias = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
        print("=*=*=*=*=*=*=*=*=*")
        print("CATEGORIAS DISPONIBLES")
        print("=*=*=*=*=*=*=*=*=*")
        for i, categoria in enumerate(categorias, 1):
            print(f"[{i}] - {categoria.name}")
        seleccion = input("Ingresa el numero de la categoria que quieres leer: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria = categorias[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    while True:
        os.system("clear")
        recetas = list(categoria.glob("*.txt"))
        if len(recetas) == 0:
            os.system("clear")
            print("Esta categoria no tiene ningun archivo")
            input("Presiona Enter para continuar...")
            return
        print(f"=*=*=*=*=*=*=*=*=*")
        print(f"RECETAS DE: {categoria.name}")
        print(f"=*=*=*=*=*=*=*=*=*")
        for i, receta in enumerate(recetas, 1):
            print(f"[{i}] - {receta.stem}")
        seleccion = input("Ingresa el numero de la receta que quieres leer: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(recetas):
            receta = recetas[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    os.system("clear")
    with open(receta, "r") as archivo:
        print(f"RECETA: {receta.stem}")
        print(f"=*=*=*=*=*=*=*=*=*")
        print(archivo.read())
    input("Presiona Enter para continuar...")

def crear_receta():
    ruta = Path(__file__).parent.parent / "recetas"
    while True:
        os.system("clear")
        categorias = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
        print("=*=*=*=*=*=*=*=*=*")
        print("CATEGORIAS DISPONIBLES")
        print("=*=*=*=*=*=*=*=*=*")
        for i, categoria in enumerate(categorias, 1):
            print(f"[{i}] - {categoria.name}")
        seleccion = input("Ingresa el numero de la categoria en la que quieres crear la receta: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria = categorias[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    os.system("clear")
    nombre_archivo = input("Cual es el nombre de tu archivo: ")
    os.system("clear")
    contenido = input("Escribe lo que quieres colocar: ")
    archivo = categoria / f"{nombre_archivo}.txt"
    if archivo.exists():
        os.system("clear")
        respuesta = input("Ya existe un archivo.txt con ese nombre, quieres reescribir su formato con la informacion que acabas de ingresar? (si/no): ")
        if respuesta.lower() in ["si", "s"]:
            with open(archivo, "w") as escritura:
                escritura.write(contenido)
            print("El archivo fue reescrito con la informacion nueva.")
            input("Presiona Enter para continuar...")
        else:
            print("No se modifico el archivo existente.")
            input("Presiona Enter para continuar...")
    else:
        with open(archivo, "w") as escritura:
            escritura.write(contenido)
        print(f"Se creo el archivo {nombre_archivo}.txt en la categoria {categoria.name}.")
        input("Presiona Enter para continuar...")

def crear_categoria():
    ruta = Path(__file__).parent.parent / "recetas"
    while True:
        os.system("clear")
        nombre_categoria = input("Cual es el nombre de la categoria que quieres crear?: ")
        nueva_categoria = ruta / nombre_categoria

        if nueva_categoria.exists():
            os.system("clear")
            print("Ya existe esa carpeta, debes elejir otro nombre.")
            input("Presiona 'enter' para intentar de nuevo...")
        else:
            nueva_categoria.mkdir()
            os.system("clear")
            print("tu carpeta fue creada")
            input("Presiona 'enter' para volver al inicio...")
            break

def eliminar_receta():
    ruta = Path(__file__).parent.parent / "recetas"
    while True:
        os.system("clear")
        categorias = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
        print("=*=*=*=*=*=*=*=*=*")
        print("CATEGORIAS DISPONIBLES")
        print("=*=*=*=*=*=*=*=*=*")
        for i, categoria in enumerate(categorias, 1):
            print(f"[{i}] - {categoria.name}")
        seleccion = input("Ingresa el numero de la categoria de la que quieres eliminar una receta: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria = categorias[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    while True:
        os.system("clear")
        recetas = list(categoria.glob("*.txt"))
        if len(recetas) == 0:
            os.system("clear")
            print("Esta categoria no tiene ningun archivo")
            input("Presiona Enter para continuar...")
            return
        print(f"=*=*=*=*=*=*=*=*=*")
        print(f"RECETAS DE: {categoria.name}")
        print(f"=*=*=*=*=*=*=*=*=*")
        for i, receta in enumerate(recetas, 1):
            print(f"[{i}] - {receta.stem}")
        seleccion = input("Cual archivo desea eliminar?: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(recetas):
            receta = recetas[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    os.system("clear")
    print(f"el archivo {receta.name} fue eliminado")
    receta.unlink()
    input("Presiona Enter para continuar...")

def eliminar_categoria():
    ruta = Path(__file__).parent.parent / "recetas"
    while True:
        os.system("clear")
        categorias = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
        print("=*=*=*=*=*=*=*=*=*")
        print("CATEGORIAS DISPONIBLES")
        print("=*=*=*=*=*=*=*=*=*")
        for i, categoria in enumerate(categorias, 1):
            print(f"[{i}] - {categoria.name}")
        seleccion = input("Cual categoria desea eliminar?: ")

        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria = categorias[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    os.system("clear")
    if any(categoria.iterdir()):
        print("la categoria tiene archivos, no se puede eliminar")
        input("Presiona Enter para continuar...")
        return
    print(f"la carpeta {categoria.name} fue eliminada")
    categoria.rmdir()
    input("Presiona Enter para continuar...")

def agregar_linea_receta():
    ruta = Path(__file__).parent.parent / "recetas"
    while True:
        os.system("clear")
        categorias = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
        print("=*=*=*=*=*=*=*=*=*")
        print("CATEGORIAS DISPONIBLES")
        print("=*=*=*=*=*=*=*=*=*")
        for i, categoria in enumerate(categorias, 1):
            print(f"[{i}] - {categoria.name}")
        seleccion = input("Ingresa el numero de la categoria de la receta que quieres modificar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria = categorias[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    while True:
        os.system("clear")
        recetas = list(categoria.glob("*.txt"))
        if len(recetas) == 0:
            os.system("clear")
            print("Esta categoria no tiene ningun archivo")
            input("Presiona Enter para continuar...")
            return
        print(f"=*=*=*=*=*=*=*=*=*")
        print(f"RECETAS DE: {categoria.name}")
        print(f"=*=*=*=*=*=*=*=*=*")
        for i, receta in enumerate(recetas, 1):
            print(f"[{i}] - {receta.stem}")
        seleccion = input("Cual receta deseas modificar?: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(recetas):
            receta = recetas[int(seleccion) - 1]
            break
        else:
            print("Seleccion invalida, intenta de nuevo.")
            input("Presiona Enter para continuar...")
    os.system("clear")
    linea = input("Escribe la nueva linea que quieres agregar al final: ")
    with open(receta, "a") as archivo:
        archivo.write(linea + "\n")
    print(f"Se agrego la linea al final de {receta.name}.")
    input("Presiona Enter para continuar...")

def menu():
    while True:
        os.system("clear")
        print("""
    ELIJE UNA OPCION:
    =*=*=*=*=*=*=*=*=*=*=*=*=*
    [1] - Leer receta
    [2] - Crear receta
    [3] - Crear categoria
    [4] - Eliminar receta
    [5] - Eliminar categoria
    [6] - Agregar una linea al final de la receta
    [7] - Finalizar programa
    =*=*=*=*=*=*=*=*=*=*=*=*=*
    """)
        opcion = input("Ingresa el numero de la opcion que quieres: ")
        if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Tiene que elejir una opcion de la patalla")
            input("Presiona Enter para continuar...")
        elif opcion == "1":
            leer_receta()
        elif opcion == "2":
            crear_receta()
        elif opcion == "3":
            crear_categoria()
        elif opcion == "4":
            eliminar_receta()
        elif opcion == "5":
            eliminar_categoria()
        elif opcion == "6":
            agregar_linea_receta()
        elif opcion == "7":
            print("Finalizando programa...")
            break

def encender_programa():
    prints()

    print(f"Esta es la cantidad de recetas: {cantidad_recets}")
    print(f"Esta es la ruta del proyecto: {rutas}")
    input("Presiona Enter para encender el programa...")
    menu()

encender_programa()