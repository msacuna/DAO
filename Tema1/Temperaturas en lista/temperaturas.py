def main():
    temperaturas = []
    cantDiasTempBajoCero = 0
    totalTemp = 0.0
    cantTemp = 0
    totalTempCalido = 0.0
    cantTempCalido = 0
    mayorTempNoCalido = None
    cantDiasMenorProm = 0

    while True:
        print("Ingrese temperaturas (50 para cortar):")
        temp = float(input())
        if temp == 50:
            break
        if -20 < temp > 49:
            print("Temperatura inválida. Ingrese nuevamente.")
            temp = float(input())
        temperaturas.append(temp)

    # cálculos
    for temperatura in temperaturas:
        if temperatura < 0:
            cantDiasTempBajoCero += 1
        totalTemp += temperatura
        cantTemp += 1

        if temperatura > 20:
            totalTempCalido += temperatura
            cantTempCalido += 1
        else:
            # actualizar mayor temperatura no cálida (<= 20)
            if mayorTempNoCalido is None or temperatura > mayorTempNoCalido:
                mayorTempNoCalido = temperatura

    promedioTemp = totalTemp / cantTemp if cantTemp != 0 else 0
    promedioTempCalido = totalTempCalido / cantTempCalido if cantTempCalido != 0 else 0

    for temperatura in temperaturas:
        if temperatura < promedioTemp:
            cantDiasMenorProm += 1

    print(f"Cantidad de días con temperatura bajo cero: {cantDiasTempBajoCero}")
    print(f"Promedio de temperaturas: {promedioTemp}")
    print(f"Promedio de temperaturas cálidas (mayores a 20 grados): {promedioTempCalido}")
    print("¿Hubo día con temperatura mayor a 40°?", "Sí" if any(t > 40 for t in temperaturas) else "No")
    if mayorTempNoCalido is not None:
        print(f"Mayor temperatura no cálida (menores o iguales a 20 grados): {mayorTempNoCalido}")
    else:
        print("No hubo temperaturas no cálidas")
    print(f"Días con temperatura menor al promedio: {cantDiasMenorProm}")

if __name__ == "__main__":
    main()