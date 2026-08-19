class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance=balance

    def __int__(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Tu numero de cuenta es: {self.numero_cuenta}")
        print(f"Tu balance es: ${self.balance:,.2f}")

    def depositar(self):
        monto=float(input("Ingrese cantidad de deposito: "))
        self.balance += monto
        print(f"Tu nuevo balance es: ${self.balance:,.2f}")
    def retirar(self):
        print(f"Tu balance es: ${self.balance:,.2f}")
        monto=float(input("Ingrese el monto a retirar: "))
        if monto > self.balance:
            print("No tienes suficiente balance.")
            return
        self.balance -= monto
        print(f"Tu nuevo balance es: ${self.balance:,.2f}")

def crear_cliente():
    nombre=input("Ingrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    numero_cuenta=input("Ingrese el numero de cuenta: ")
    balance=float(input("Ingrese el balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)
def inicio():
    cliente=crear_cliente()
    opcion=0
    while opcion!=3:
        print(f"""
        BANCO
        Balance actual: ${cliente.balance:,.2f}
        [1] - Ingresar monto
        [2] - Sacar dinero
        [3] - Finalizar
        """)
        opcion=int(input("Seleccione una opcion: "))
        if opcion==1:
            cliente.depositar()
        elif opcion==2:
            cliente.retirar()
        elif opcion==3:
            print("Cerrando sesion...")
inicio()