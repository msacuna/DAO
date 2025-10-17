from Hospital import Hospital, AtencionMedica, AtencionFarmacia, Paciente

def main():
    # Crear pacientes
    paciente1 = Paciente("Juan Perez", "Dolor de cabeza", True)
    paciente2 = Paciente("Maria Lopez", "Fiebre", False)

    # Crear atenciones
    atencion1 = AtencionMedica(1, 2, "Consulta médica", paciente1, 1000)
    atencion2 = AtencionMedica(2, 1, "Consulta médica", paciente2, 800)
    atencion3 = AtencionFarmacia(3, 2, "Compra medicamentos", 500, 50)

    # Crear hospital y agregar atenciones
    hospital = Hospital("Hospital Central", [])
    hospital.addAtencion(atencion1)
    hospital.addAtencion(atencion2)
    hospital.addAtencion(atencion3)

    # Calcular importe total de atenciones médicas
    total_medicas = hospital.calcularImporteTotalAtencion()
    print(f"Importe total de atenciones médicas: {total_medicas}")

    # Calcular importe promedio de atenciones médicas en un rango
    promedio = hospital.calcularImportePromAtenciones(500, 1500)
    print(f"Importe promedio de atenciones médicas en el rango 500-1500: {promedio}")

    # Devolver el código de la primera atención de un paciente habitual
    codigo_habitual = hospital.devolverCodPrimAtencHabitual()
    print(f"Código de la primera atención de un paciente habitual: {codigo_habitual}")

if __name__ == "__main__":
    main()