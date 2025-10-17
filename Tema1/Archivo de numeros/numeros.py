def listaNumPares(numeros):
    listaPares = []
    for num in numeros:
        if num % 2 == 0:
            listaPares.append(num)
    return listaPares


def cantNumMayoresPromedio(numeros, promedio):
    cantNum = 0
    for num in numeros:
        if num > promedio:
            cantNum += 1
    return cantNum


def promedioNumeros(numeros):
    cantNum = totalNum = 0
    for num in numeros:
        cantNum += 1
        totalNum += num
    if cantNum == 0:
        return 0
    return totalNum / cantNum


def leerArchivo(nombreArchivo):
    numeros = []
    archivo = open(nombreArchivo, "r")
    while True:
        linea = archivo.readline()
        if not linea:
            break
        numeros.append(int(linea[:-1]))
    archivo.close()
    return numeros

def main():
    lista = leerArchivo('numeros.txt')
    promedio = promedioNumeros(lista)
    cantNum = cantNumMayoresPromedio(lista, promedio)
    listaPares = listaNumPares(lista)

    for num in lista:
        print(num)

    print("El promedio es de todos los números es:", promedio)
    print("La cantidad de números mayores al promedio es:", cantNum)
    print("La lista de números pares es:")
    for x in listaPares:
        print(x)


if __name__ == "__main__":
    main()