def main():
    totalLitrosSuper = totalLitrosEspecial = totalLitrosGasoil = cantCombMin = surtMinComb = 0
    for surtidor in range(10):
        numSurtidor = int(input("Ingrese número de surtidor(1-30):"))
        if 1 < numSurtidor < 30:
            print("Surtidor válido")
            numSurtidor = int(input("Ingrese número de surtidor(1-30):"))
        
        cantLitros = float(input("Ingrese cantidad de litros:"))
        if cantLitros < 0:
            print("Cantidad inválida")
            cantLitros = float(input("Ingrese cantidad de litros:"))
        
        tipoCombustible = int(input("Ingrese tipo de combustible(1: Nafta Super, 2: Nafta Especial, 3: Gasoil):"))
        if tipoCombustible != 1 and tipoCombustible != 2 and tipoCombustible != 3:
            print("Tipo de combustible inválido")
            tipoCombustible = int(input("Ingrese tipo de combustible(1: Nafta Super, 2: Nafta Especial, 3: Gasoil):"))
        
        # calculos
        if tipoCombustible == 1:
            totalLitrosSuper += cantLitros
        elif tipoCombustible == 2:
            totalLitrosEspecial += cantLitros
        else:
            totalLitrosGasoil += cantLitros
        
        if surtidor == 1:
            cantCombMin = cantLitros
        elif cantLitros < cantCombMin:
            cantCombMin = cantLitros
            surtMinComb = numSurtidor

        totalLitros = totalLitrosSuper + totalLitrosEspecial + totalLitrosGasoil
        promedio = totalLitros / 10


    # resultados
    print(f"Total litros Nafta Super: {totalLitrosSuper}")
    print(f"Total litros Nafta Especial: {totalLitrosEspecial}")
    print(f"Total litros Gasoil: {totalLitrosGasoil}")
    print(f"Surtidor que vendió menor cantidad de combustible: {surtMinComb} con {cantCombMin} litros")
    print(f"Promedio de litros vendidos por surtidor: {promedio}")

if __name__ == "__main__":
    main()