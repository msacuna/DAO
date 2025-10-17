import Personas1

def main():
    personas = []

    while True:
        print("Ingrese los datos de la persona (o escriba 'salir' para finalizar):")
        nombre = input("Nombre: ")
        if nombre.lower() == 'salir':
            break
        apellido = input("Apellido: ")
        documento = input("Documento: ")
        edad = int(input("Edad: "))

        # Crear instancia de Personas1 y mostrar su estado
        persona = Personas1.Personas1(nombre, apellido, documento, edad)
        print(persona)

        # Guardar la persona en la lista
        personas.append(persona)

    # Determinar la persona de menor edad
    if personas:
        menor_edad = personas[0]
        for persona in personas:
            if persona.edad < menor_edad.edad:
                menor_edad = persona
        print("\nLa persona de menor edad es:")
        print(menor_edad)
    else:
        print("No se ingresaron personas.")

if __name__ == "__main__":
    main()