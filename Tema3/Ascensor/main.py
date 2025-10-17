import Ascensor

def main():
    print("Ingrese cantidad máxima de personas que puede contener el ascensor:")
    capacMax = int(input())
    print("Ingrese cantidad de pisos del edificio:")
    cantPisos = int(input())
    ascensor = Ascensor.Ascensor(capacMax, cantPisos)

    print("Ingrese el piso al que desea desplazarse (0 a", cantPisos - 1, "):")
    pisoDestino = int(input())
    pisoDestino = ascensor.ir_a_piso(pisoDestino)
    print(pisoDestino)

    print("Ingrese la cantidad de personas que desean subir al ascensor:")
    cantPersonasSubir = int(input())
    resultadoSubir = ascensor.subir_personas(cantPersonasSubir)
    print(resultadoSubir)

    print("Ingrese la cantidad de personas que desean bajar del ascensor:")
    cantPersonasBajar = int(input())
    resultadoBajar = ascensor.bajar_personas(cantPersonasBajar)
    print(resultadoBajar)

    estadoAscensor = ascensor.toString()

if __name__ == "__main__":
    main()