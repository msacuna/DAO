from abc import ABC, abstractmethod

class Cuenta (ABC):
    def __init__(self, numero, nombre, saldo):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def extraer(self, monto):
        pass

class CuentaAhorro (Cuenta):
    def __init__(self, numero, nombre, saldo):
        super().__init__(numero, nombre, saldo)

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Saldo actual: {self.saldo}."

    def extraer(self, monto):
        if monto > self.saldo:
            return "No se puede extraer, no hay suficiente saldo."
        else:
            self.saldo -= monto
            return f"Extracción exitosa. Saldo restante: {self.saldo}."

class CuentaCorriente (Cuenta):
    def __init__(self, numero, nombre, saldo, acuerdo):
        super().__init__(numero, nombre, saldo)
        self.acuerdo = acuerdo

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Saldo actual: {self.saldo}."

    def extraer(self, monto):
        if monto > self.saldo + self.acuerdo:
            return "No se puede extraer, no hay suficiente saldo y acuerdo."
        else:
            self.saldo -= monto
            return f"Extracción exitosa. Saldo restante: {self.saldo}."