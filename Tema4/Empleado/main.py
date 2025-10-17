from Empleado import EmpleadoObrero, EmpleadoAdministrativo, EmpleadoVendedor, Empleado

tipoEmpleadoMap = {"1": "Obrero", "2": "Administrativo", "3": "Vendedor"}  # Mapeo de tipos de empleados

def leerArchivo(nombreArchivo):
    lista = []
    try:
        archivo = open(nombreArchivo, "r")
        while True:
            linea = archivo.readline()
            if not linea:
                break
            datos = linea.strip().split(";")  # Cambiado el delimitador a punto y coma
            if len(datos) == 6:
                tipoEmpleado, legajo, nombre, apellido, sueldoBasico, extra = datos
                tipoEmpleado = tipoEmpleadoMap.get(tipoEmpleado, tipoEmpleado)  # Convertir número a tipo de empleado
                if tipoEmpleado == "Obrero":
                    empleado = EmpleadoObrero(tipoEmpleado, int(legajo), nombre, apellido, float(sueldoBasico), int(extra))
                elif tipoEmpleado == "Administrativo":
                    cobrarPresentismo = extra.lower() == 'true'
                    empleado = EmpleadoAdministrativo(tipoEmpleado, int(legajo), nombre, apellido, float(sueldoBasico), cobrarPresentismo)
                elif tipoEmpleado == "Vendedor":
                    empleado = EmpleadoVendedor(tipoEmpleado, int(legajo), nombre, apellido, float(sueldoBasico), float(extra))
                else:
                    print(f"Tipo de empleado desconocido: {tipoEmpleado}")
                    continue
                lista.append(empleado)
            else:
                print(f"Línea ignorada por formato incorrecto: {linea.strip()}")
                print(f"Datos procesados: {datos}")  # Depuración adicional para ver los datos procesados
        archivo.close()
    except FileNotFoundError:
        print(f"El archivo {nombreArchivo} no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return lista

def main():
    # Leer empleados desde el archivo
    empleados = leerArchivo("empleados.csv")

    # Calcular el total a pagar de sueldos
    totalSueldos = Empleado.calcularTotalSueldos(empleados)
    print(f"Total a pagar en sueldos: {totalSueldos}")

    # Contar empleados por tipo
    conteoPorTipo = Empleado.contarEmpleadosPorTipo(empleados)
    print("Cantidad de empleados por tipo:")
    for tipo, cantidad in conteoPorTipo.items():
        print(f"{tipo}: {cantidad}")

    # Buscar un empleado por legajo y mostrar su sueldo
    legajoBuscar = int(input("Ingrese el legajo del empleado a buscar: "))
    empleado = Empleado.buscarEmpleadoPorLegajo(empleados, legajoBuscar)
    if empleado:
        print(f"El sueldo del empleado con legajo {legajoBuscar} es: {empleado.calcularSueldo()}")
    else:
        print(f"No se encontró un empleado con el legajo {legajoBuscar}")

if __name__ == "__main__":
    main()