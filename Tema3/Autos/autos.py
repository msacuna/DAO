class Auto():
    def __init__(self, marca, modelo, color, cantCombustible):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cantCombustible = cantCombustible  
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"
    
    def conducir(self, cantKm):
        if self.cantCombustible <= 0:
            return "No se puede conducir, no hay combustible."
        consumo = (cantKm * 1) / 11
        if consumo > self.cantCombustible:
            return "No se puede conducir, no hay suficiente combustible."
        else:
            self.cantCombustible -= consumo
            return f"Se puede conducir. Combustible restante: {self.cantCombustible:.2f} litros."
    
    def cargarCombustible(self, cantLitros):
        self.cantCombustible += cantLitros
        if self.cantCombustible > 54:
            print("Tanque lleno. Exceso de combustible no se puede cargar. Se devuelve la cantidad de litros derramados")
            return self.cantCombustible - 54
        return print(f"Tanque lleno. Cantidad de litros: {self.cantCombustible} litros.")