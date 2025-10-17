from functools import reduce

def main():
    lista = ["Aruba","Jamaica","Bermuda","Bahama","Key Largo","Montigo"]
    letraInicialCadaPalabra = list(map(lambda x: x[0], lista))
    longitudCadaPalabra = list(map(len, lista))
    cantLetras = reduce(lambda x, y: x + y, longitudCadaPalabra)

    print("Letra inicial de cada palabra:", letraInicialCadaPalabra)
    print("Longitud de cada palabra:", longitudCadaPalabra)
    print("Cantidad total de letras:", cantLetras)

if __name__ == "__main__":
    main()

