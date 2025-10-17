from functools import reduce

def suma(x, y):
    return x + y

def esNegativo(num):
    return num < 0

def main():
    numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cuadrados = list(map(lambda x: x**2, numeros))
    negativos = list(filter(esNegativo, numeros))
    total = reduce(suma, numeros)

    print("Cuadrados de los números:", cuadrados)
    print("Números negativos:", negativos)
    print("Suma total de los números:", total)

if __name__ == "__main__":
    main()