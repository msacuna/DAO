from Cuenta import CuentaAhorro, CuentaCorriente

def main():
    cuentas = []

    # Cargar cuentas bancarias
    while True:
        tipo = input("Ingrese el tipo de cuenta (ahorro/corriente) o 'salir' para finalizar: ").lower()
        if tipo == 'salir':
            break

        numero = int(input("Número de cuenta: "))
        nombre = input("Nombre del titular: ")
        saldo = float(input("Saldo inicial: "))

        if tipo == 'ahorro':
            cuenta = CuentaAhorro(numero, nombre, saldo)
        elif tipo == 'corriente':
            acuerdo = float(input("Acuerdo de descubierto: "))
            cuenta = CuentaCorriente(numero, nombre, saldo, acuerdo)
        else:
            print("Tipo de cuenta no válido.")
            continue

        cuentas.append(cuenta)

    # Realizar operaciones
    while True:
        operacion = input("Ingrese operación (depositar/extraer) o 'salir' para finalizar: ").lower()
        if operacion == 'salir':
            break

        numero = int(input("Número de cuenta: "))
        monto = float(input("Monto: "))

        cuenta = next((c for c in cuentas if c.numero == numero), None)
        if not cuenta:
            print("Cuenta no encontrada.")
            continue

        if operacion == 'depositar':
            print(cuenta.depositar(monto))
        elif operacion == 'extraer':
            print(cuenta.extraer(monto))
        else:
            print("Operación no válida.")

    # Mostrar listado final de cuentas
    print("\nListado de cuentas con saldos definitivos:")
    for cuenta in cuentas:
        print(f"Cuenta {cuenta.numero} - Titular: {cuenta.nombre} - Saldo: {cuenta.saldo}")

if __name__ == "__main__":
    main()