class Personas1():
    def __init__(self, nombre, apellido, documento, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Documento: {self.documento}, Edad: {self.edad}"
    