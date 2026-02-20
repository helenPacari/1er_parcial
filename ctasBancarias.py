cuentas = []

class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def mostrar_info(self):
        print("------------------------------------------------")
        print("1er PARCIAL - Taller de Aplicaciones en Internet")
        print("------------------------------------------------")
        print("Titular:", self.titular)
        print("Número de cuenta:", self.numeroCuenta)
        print("Saldo:", self.saldo)
        print("---------------")

    def depositar(self, monto):
        self.saldo += monto
        print("Depósito realizado ¡exitosamente!")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retiro realizado ¡exitosamente!")
        else:
            print("Error: Saldo insuficiente")

# Creando función para crear cuentas
def crear_cuenta():
    titular = input("Ingrese nombre del titular: ")
    nroCuenta = input("Ingrese número de cuenta: ")
    saldo = float(input("Ingrese saldo inicial: "))

    nuevaCuenta = CuentaBancaria(titular, nroCuenta, saldo)
    cuentas.append(nuevaCuenta)

    print("Cuenta creada ¡exitosamente!")


# Creando función para mostrar cuentas
def mostrar_cuentas():
    if len(cuentas) == 0:
        print("No hay cuentas registradas.")
    else:
        for cuenta in cuentas:
            cuenta.mostrar_info()


# Creando función para realizar depósito
def realizar_deposito():
    numero = input("Ingrese número de cuenta: ")
    for cuenta in cuentas:
        if cuenta.numeroCuenta == numero:
            monto = float(input("Ingrese monto a depositar: "))
            cuenta.depositar(monto)
            return
    print("La cuenta no fue encontrada.")

# Creando función para realizar retiro
def realizar_retiro():
    numero = input("Ingrese el número de cuenta: ")
    for cuenta in cuentas:
        if cuenta.numeroCuenta == numero:
            monto = float(input("Ingrese monto a retirar: "))
            if monto > cuenta.saldo:
                print("Error: No tiene saldo suficiente.")
            else:
                cuenta.retirar(monto)
            return
    print("La cuenta no fue encontrada.")


# Creando menú interactivo
while True:
    print("\n===== MENÚ =====")
    print("1. Crear cuenta")
    print("2. Mostrar cuentas")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        mostrar_cuentas()
    elif opcion == "3":
        realizar_deposito()
    elif opcion == "4":
        realizar_retiro()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")