from abc import ABC, abstractmethod

class Universidad():
    def __init__(self, archivo_cursos):
        try:
            self.cursos = leerArchivo(archivo_cursos)
        except FileNotFoundError:
            raise FileNotFoundError("El archivo especificado no existe.")
    
    def cantidad_por_tipo(self,):
        conteo = {"Teorico": 0, "Practico": 0, "Online": 0}
        for c in self.cursos:
            tipo = type(c).__name__
            if tipo in conteo:
                conteo[tipo] += 1
        return conteo
    
    def calcular_promedio_precio_por_estudiante(self):
        total_precio = 0
        total_alumnos = 0
        for curso in self.cursos:
            total_precio += curso.calcular_precio()
            total_alumnos += curso.cantidad_alumnos
        promedio = total_precio // total_alumnos if total_alumnos > 0 else 0
        return promedio
    
    def calcular_ingreso_total(self):
        total_ingreso = 0
        for curso in self.cursos:
            total_ingreso += curso.calcular_precio_total()
        return total_ingreso
    
    def contar_teoricos_mas_50_alumnos(self):
        contador = 0
        for curso in self.cursos:
            if isinstance(curso, Teorico) and curso.cantidad_alumnos > 50:
                contador += 1
        return contador
    
    def contar_online_con_tutorias(self):
        contador = 0
        for curso in self.cursos:
            if isinstance(curso, Online) and curso.incluye_tutorias:
                contador += 1
        return contador
    
    def obtener_curso_mas_caro(self):
        if not self.cursos:
            return None
        return max(self.cursos, key=lambda c: c.calcular_precio())

class Curso(ABC):
    def __init__(self, tipo, codigo, nombre, precio_base, cantidad_alumnos):
        self.tipo = tipo
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.cantidad_alumnos = cantidad_alumnos
    
    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def calcular_precio_total(self):
        pass

class Teorico(Curso):
    def __init__(self, codigo, nombre, precio_base, cantidad_alumnos):
        super().__init__(1, codigo, nombre, precio_base, cantidad_alumnos)

    def calcular_precio(self):
        precio_total = self.precio_base   
        return precio_total
    
    def calcular_precio_total(self):
        importe_base = Teorico.calcular_precio(self)
        precio_total = importe_base * self.cantidad_alumnos        
        if self.cantidad_alumnos > 50:
            precio_total = self.precio_base * self.cantidad_alumnos * 0.9
        return precio_total

class Practico(Curso):
    def __init__(self, codigo, nombre, precio_base, cantidad_alumnos, practicas_laboratorio):
        super().__init__(2, codigo, nombre, precio_base, cantidad_alumnos)
        self.practicas_laboratorio = practicas_laboratorio

    def calcular_precio(self):
        precio_total = self.precio_base
        precio_total += 500 * self.practicas_laboratorio
        return precio_total
    
    def calcular_precio_total(self):
        importe_base = Practico.calcular_precio(self)
        precio_total = importe_base * self.cantidad_alumnos
        return precio_total

class Online(Curso):
    def __init__(self, codigo, nombre, precio_base, cantidad_alumnos, incluye_tutorias):
        super().__init__(3, codigo, nombre, precio_base, cantidad_alumnos)
        self.incluye_tutorias = incluye_tutorias
    
    def calcular_precio(self):
        precio_total = self.precio_base * self.cantidad_alumnos
        if self.incluye_tutorias:
            precio_total *= 1.15
        return precio_total
    
    def calcular_precio_total(self):
        importe_base = Online.calcular_precio(self)
        precio_total = importe_base * self.cantidad_alumnos
        return precio_total

def leerArchivo(nombreArchivo):
    cursos = []
    with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            tipo, codigo, nombre, precio_base, cantidad_alumnos, extra = linea.strip().split(',')
            
            tipo = int(tipo) 
            precio_base = float(precio_base)
            cantidad_alumnos = int(cantidad_alumnos)
            if tipo == 1:  
                curso = Teorico(codigo, nombre, precio_base, cantidad_alumnos)
            elif tipo == 2:
                practicas_laboratorio = int(extra)
                curso = Practico(codigo, nombre, precio_base, cantidad_alumnos, practicas_laboratorio)
            elif tipo == 3:  
                incluye_tutorias = True if extra.strip().lower() == 'true' else False
                curso = Online(codigo, nombre, precio_base, cantidad_alumnos, incluye_tutorias)
            else:
                continue
            cursos.append(curso)
    return cursos
    
def main():
    universidad = Universidad("cursos.csv")
    print("Promedio precio por estudiante:", universidad.calcular_promedio_precio_por_estudiante())
    curso_mas_caro = universidad.obtener_curso_mas_caro()
    print("Curso más caro:", curso_mas_caro.codigo, curso_mas_caro.nombre, "Precio:", curso_mas_caro.calcular_precio())
    print("Ingreso total:", universidad.calcular_ingreso_total())
    print("Cantidad de cursos teóricos con más de 50 alumnos:", universidad.contar_teoricos_mas_50_alumnos())
    print("Cantidad de cursos online con tutorías:", universidad.contar_online_con_tutorias())
    print("Cantidad de cursos por tipo:", universidad.cantidad_por_tipo())


if __name__ == "__main__":
    main()