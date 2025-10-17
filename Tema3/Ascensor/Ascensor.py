class Ascensor():
    def __init__(self, capacMax, cantPisos):
        self.capacMax = capacMax
        self.cantPisos = cantPisos
        self.pisoActual = 0
        self.cantPersonas = 0  
    
    def ir_a_piso(self, pisoDestino):
        if pisoDestino < 0 or pisoDestino >= self.cantPisos:
            return "El piso destino no es válido."
        if pisoDestino == self.pisoActual:
            return "El ascensor ya está en el piso destino."
        self.pisoActual = pisoDestino
        return f"Ascensor desplazado al piso {self.pisoActual}."
    
    def subir_personas(self, cantPersonas):
        if cantPersonas < 0:
            return -1
        if self.cantPersonas + cantPersonas > self.capacMax:
            return "No se pueden subir más personas, capacidad máxima excedida. Aquí solo entran hasta " + str(self.capacMax - self.cantPersonas) + " personas."
        self.cantPersonas += cantPersonas
        return f"Subieron {cantPersonas} personas. Cantidad actual: {self.cantPersonas}."
    
    def bajar_personas(self, cantPersonas):
        if cantPersonas < 0:
            return -1
        if cantPersonas > self.cantPersonas:
            return "Todas las personas salen: " + str(self.cantPersonas) + " personas."
        self.cantPersonas -= cantPersonas
        return f"Bajaron {cantPersonas} personas. Cantidad actual: {self.cantPersonas}."
    
    def toString(self):
        return f"El ascensor está en el piso {self.pisoActual}, Cantidad de personas: {self.cantPersonas}."
    