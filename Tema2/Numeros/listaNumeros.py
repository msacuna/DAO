import random

def calcularImpares(numeros):
    impares = []
    for n in numeros:
        if n % 2 != 0:
            impares.append(n)
    return impares

def calcularImpares(numeros):
    impares = []
    cantImpares = totalImpares = prom = 0
    for n in numeros:
        if n % 2 != 0:
            impares.append(n)
    return impares

def calcularCantPares(numeros):
    cantPares = 0
    for n in numeros:
        if n % 2 == 0:
            cantPares += 1
    return cantPares

def calcularMenor(a, b):
    if a < b:
        return a
    return b

def main():
    numeros = cuadrados = multiplos7 = []
    totalImpares = 0 
    for num in range(1000):
        numero = random.randint(-1000000 , 1000000)
        numeros.append(numero)

    menor = numeros[0]
    for n in numeros:
        menor = calcularMenor(menor, n)
        pares = calcularCantPares(numeros)
        if 10 <= n <= 100:
            cuadrados = list(map(lambda x: x**2, n))
        if n % 7 == 0:
            multiplos7.append(n)
            multiplos7.sort(reverse=True)
        
    
    impares = calcularImpares(numeros)
    for n in impares:
        totalImpares += n
    cantImpares = len(impares)
    prom = totalImpares / cantImpares if cantImpares > 0 else 0


    

    print(f"El número menor es: {menor}")
    print(f"La cantidad de números pares es: {pares}")
    print(f"Promedio de números impares: {prom}")
    print(f"Cuadrados de los números entre 10 y 100: {cuadrados}")
    print(f"Múltiplos de 3 del punto anterior: ")
    for c in cuadrados:
        if c % 3 == 0:
            print(c)
    print(f"Multiplos de 7 ordenados descendentemente: {multiplos7}")

    



if __name__ == "__main__":
    main()