from abc import ABC, abstractmethod

class Hospital():
    def __init__(self, razonSocial, atenciones):
        self.razonSocial = razonSocial
        self.atenciones = atenciones

    def addAtencion(self, atencion):
        self.atenciones.append(atencion)

    def calcularImporteTotalAtencion(self):
        total = 0
        for atencion in self.atenciones:
            if isinstance(atencion, AtencionMedica):
                total += atencion.calcularImporte()
        return total

    def calcularImportePromAtenciones(self, numA, numB):
        total = cant = 0
        for atencion in self.atenciones:
            if isinstance(atencion, AtencionMedica) and numA <= atencion.importe <= numB:
                total += atencion.calcularImporte()
                cant += 1
        if cant > 0:
            return total / cant
        else:
            return 0
    
    def devolverCodPrimAtencHabitual(self):
        for atencion in self.atenciones:
            if isinstance(atencion, AtencionMedica) and atencion.paciente.PacienteHabitual:
                return atencion.codigo
        return 0

class Atencion(ABC):
    def __init__(self, codigo, tipoCobro, tipoAtencion):
        self.codigo = codigo
        self.tipoCobro = tipoCobro
        self.tipoAtencion = tipoAtencion
    
    @abstractmethod
    def calcularImporte(self):
        pass
    
class AtencionMedica(Atencion):
    def __init__(self, codigo, tipoCobro, tipoAtencion, paciente, importe):
        super().__init__(codigo, tipoCobro, tipoAtencion)
        self.paciente = paciente
        self.importe = importe
    
    def toString(self):
        return f"Código: {self.codigo}, Tipo de cobro: {self.tipoCobro}, Tipo de atención: {self.tipoAtencion}, Paciente: {self.paciente.toString()}, Importe: {self.importe}"
    
    def getCodigo(self):
        return self.codigo
    
    def getTipoCobro(self):
        return self.tipoCobro
    
    def getTipoAtencion(self):
        return self.tipoAtencion
    
    def getPaciente(self):
        return self.paciente
    
    def getImporte(self):
        return self.importe
    
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setTipoCobro(self, tipoCobro):
        self.tipoCobro = tipoCobro
    
    def setPaciente(self, paciente):
        self.paciente = paciente
    
    def setImporte(self, importe):
        self.importe = importe
    
    def calcularImporte(self):
        importeFinal = self.importe
        if self.paciente.PacienteHabitual:
            importeFinal *= 0.75 #descuento 25%
        if self.tipoCobro == 2:
            importeFinal *= 1.20 # aumento 20%
            return importeFinal
        else:
            importeFinal *= 0.9 # descuento 10%
            return importeFinal
    
class AtencionFarmacia(Atencion):
    def __init__(self, codigo, tipoCobro, tipoAtencion, impTotalMedicamentos, cuponDesc):
        super().__init__(codigo, tipoCobro, tipoAtencion)
        self.impTotalMedicamentos = impTotalMedicamentos
        self.cuponDesc = cuponDesc
    
    def toString(self):
        return f"Código: {self.codigo}, Tipo de cobro: {self.tipoCobro}, Tipo de atención: {self.tipoAtencion}, Importe total medicamentos: {self.impTotalMedicamentos}, Cupón de descuento: {self.cuponDesc}"
    
    def getCodigo(self):
        return self.codigo
    
    def getTipoCobro(self):
        return self.tipoCobro
    
    def getTipoAtencion(self):
        return self.tipoAtencion
    
    def getImpTotalMedicamentos(self):
        return self.impTotalMedicamentos
    
    def getCuponDesc(self):
        return self.cuponDesc
    
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setTipoCobro(self, tipoCobro):
        self.tipoCobro = tipoCobro
    
    def setImpTotalMedicamentos(self, impTotalMedicamentos):
        self.impTotalMedicamentos = impTotalMedicamentos
    
    def setCuponDesc(self, cuponDesc):
        self.cuponDesc = cuponDesc
    
    def calcularImporte(self):
        importeFinal = self.impTotalMedicamentos
        if self.cuponDesc:
            importeFinal = self.impTotalMedicamentos - self.cuponDesc
        if self.tipoCobro == 2:
            importeFinal *= 1.30
            return importeFinal
        else:
            importeFinal *= 0.95
            return importeFinal        

class Paciente():
    def __init__(self, nombre, sintoma, PacienteHabitual):
        self.nombre = nombre
        self.sintoma = sintoma
        self.PacienteHabitual = PacienteHabitual
    
    def toString(self):
        return f"Nombre: {self.nombre}, Sintoma: {self.sintoma}, Paciente Habitual: {self.PacienteHabitual}"
    
    def getNombre(self):
        return self.nombre
    
    def getSintoma(self):   
        return self.sintoma
    
    def getPacienteHabitual(self):
        return self.PacienteHabitual

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setSintoma(self, sintoma):
        self.sintoma = sintoma
    
    def setPacienteHabitual(self, PacienteHabitual):
        self.PacienteHabitual = PacienteHabitual
