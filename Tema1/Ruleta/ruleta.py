import random
from rich.console import Console

console = Console()

def mostrarTirada(numero: int, color: str):
    if color == "verde":
        console.print(f"Se obtuvo [bold white on green]{numero}{color}[/]")
    elif color == "rojo":
        console.print(f"Se obtuvo [bold white on red]{numero}{color}[/]")
    else:
        console.print(f"Se obtuvo [bold white on black]{numero}{color}[/]")

def mostrarRuleta(ruleta: list[(int, str)]):
    col = 1
    for numero, color in ruleta:
        if color == "verde":
            console.print(f"[bold white on green]{numero:^12}[/]", end="")
            print()
        elif color == "rojo":
            console.print(f"[bold white on red]{numero:^4}[/]", end="")
        else:
            console.print(f"[bold white on black]{numero:^4}[/]", end="")
            col += 1
        
        if col == 4:
            print()
            col = 1

def reducirNumero(numero: int) -> int:
    if numero < 10:
        return numero
    
    # convertir numero en lista de digitos
    digitos = [int(difito) for difito in str(numero)]
    # calcular suma de digitos
    suma = sum(digitos)
    return reducirNumero(suma)

def buscarColor(numero: int) -> str:
    if numero == 0:
        return "verde"
    elif numero == 10 or numero == 28:
        return "negro"
    else:
        if reducirNumero(numero) % 2 == 0:
            return "negro"
        else:
            return "rojo"


def generarRuleta():
    ruleta = []
    for num in range(0, 37):
        ruleta.append((num, buscarColor(num)))
    return ruleta

def tirada(ruleta: list[(int, str)]):
    cantPares = cantImpares = cantRojos = cantNegros = tiradasPrimDoc = tiradasSegDoc = tiradasTercDoc = cantCeros = 0
    jugadas = 1000
    numTirada = colorTirada = None

    for i in range(jugadas):
        numTirada = random.randint(0, 36)
        colorTirada = ruleta[numTirada][1]
        mostrarTirada(numTirada, colorTirada)

        if (numTirada % 2) == 0:
            cantPares += 1
        else:
            cantImpares += 1
        if colorTirada == "rojo":
            cantRojos += 1
        elif colorTirada == "negro":
            cantNegros += 1
        else:
            cantCeros += 1
        
        docena = numTirada // 12
        if docena == 1:
            tiradasPrimDoc += 1
        elif docena == 2:
            tiradasSegDoc += 1
        else:
            tiradasTercDoc += 1
        
        porcenCeros = (cantCeros / jugadas) * 100

        print(f"Resultados de {jugadas} jugadas:")
        print(f"Cantidad de números pares: {cantPares}")
        print(f"Cantidad de números impares: {cantImpares}")
        print(f"Cantidad de tiradas primer docena: {tiradasPrimDoc}")
        print(f"Cantidad de tiradas segunda docena: {tiradasSegDoc}")
        print(f"Cantidad de tiradas tercera docena: {tiradasTercDoc}")
        print(f"Porcentaje de ceros: {porcenCeros}%")
        print(f"Cantidad de números rojos:", "[bold white on red]"+str(cantRojos))
        print(f"Cantidad de números negros:", "[bold white on black]"+str(cantNegros))


def main():
    ruleta = generarRuleta()
    mostrarRuleta(ruleta)
    tirada(ruleta)

if __name__ == "__main__":
    main()