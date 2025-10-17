from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, tipoEmpleado, legajo, nombre, apellido, sueldoBasico):
        self.tipoEmpleado = tipoEmpleado
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldoBasico = sueldoBasico
    
    @abstractmethod
    def calcularSueldo(self):
        pass

    @staticmethod
    def calcularTotalSueldos(listaEmpleados):
        totalSueldos = 0
        for empleado in listaEmpleados:
            totalSueldos += empleado.calcularSueldo()
        return totalSueldos

    @staticmethod
    def contarEmpleadosPorTipo(listaEmpleados):
        conteo = {}
        for empleado in listaEmpleados:
            if empleado.tipoEmpleado in conteo:
                conteo[empleado.tipoEmpleado] += 1
            else:
                conteo[empleado.tipoEmpleado] = 1
        return conteo

    @staticmethod
    def buscarEmpleadoPorLegajo(listaEmpleados, legajo):
        for empleado in listaEmpleados:
            if empleado.legajo == legajo:
                return empleado
        return None

class EmpleadoObrero(Empleado):
    def __init__(self, tipoEmpleado, legajo, nombre, apellido, sueldoBasico, diasTrabajadosXMes):
        super().__init__(tipoEmpleado, legajo, nombre, apellido, sueldoBasico)
        self.diasTrabajadosXMes = diasTrabajadosXMes
    
    def calcularSueldo(self):
        sueldoTotal = (self.sueldoBasico / 20) * self.diasTrabajadosXMes
        return sueldoTotal

class EmpleadoAdministrativo(Empleado):
    def __init__(self, tipoEmpleado, legajo, nombre, apellido, sueldoBasico, cobrarPresentismo):
        super().__init__(tipoEmpleado, legajo, nombre, apellido, sueldoBasico)
        self.cobrarPresentismo = cobrarPresentismo
    
    def calcularSueldo(self):
        sueldoTotal = 0
        if self.cobrarPresentismo:
            sueldoTotal = self.sueldoBasico * 1.13
        else:
            sueldoTotal = self.sueldoBasico
        return sueldoTotal

class EmpleadoVendedor(Empleado):
    def __init__(self, tipoEmpleado, legajo, nombre, apellido, sueldoBasico, importeTotalXMes):
        super().__init__(tipoEmpleado, legajo, nombre, apellido, sueldoBasico)
        self.importeTotalXMes = importeTotalXMes
    
    def calcularSueldo(self):
        sueltoTotal = 0
        porcTotalVendido = (self.importeTotalXMes * 0.01)
        sueltoTotal = self.sueldoBasico + porcTotalVendido
        return sueltoTotal
