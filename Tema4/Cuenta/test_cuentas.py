from Cuenta import CuentaAhorro, CuentaCorriente

def main():
    # Crear una cuenta de ahorro
    cuenta_ahorro = CuentaAhorro(1, "Juan Perez", 1000)
    print(cuenta_ahorro.depositar(500))
    print(cuenta_ahorro.extraer(200))
    print(cuenta_ahorro.extraer(1500))

    # Crear una cuenta corriente
    cuenta_corriente = CuentaCorriente(2, "Maria Lopez", 500, 1000)
    print(cuenta_corriente.depositar(300))
    print(cuenta_corriente.extraer(600))
    print(cuenta_corriente.extraer(2000))

if __name__ == "__main__":
    main()