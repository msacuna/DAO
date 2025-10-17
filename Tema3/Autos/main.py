import autos

def main():
    # Crear instancia correctamente usando el módulo 'autos'
    mi_auto = autos.Auto("Toyota", "Corolla", "Rojo", 50)
    # Imprimir representación del auto (usa __str__ internamente)
    print(mi_auto)
    # Llamar al método conducir y mostrar su resultado
    resultado = mi_auto.conducir(100)
    print(resultado)
    # Llamar al método cargarCombustible y mostrar su resultado
    resultado_carga = mi_auto.cargarCombustible(10)


if __name__ == "__main__":
    main()