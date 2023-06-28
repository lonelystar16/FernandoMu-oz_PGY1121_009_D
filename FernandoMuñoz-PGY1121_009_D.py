def validar_nif(nif):
     return True

def grabar_persona(personas):
    nif = input("Ingrese el NIF de la persona: ")
    if not validar_nif(nif):
        print("El NIF ingresado es incorrecto.")
        return
    
    nombre = input("Ingrese el nombre de la persona: ")
    if len(nombre) < 8:
        print("El nombre debe tener al menos 8 caracteres.")
        return
    
    edad = int(input("Ingrese la edad de la persona: "))
    if edad < 0:
        print("La edad debe ser mayor o igual a 0.")
        return
    
    persona = {
        'NIF': nif,
        'Nombre': nombre,
        'Edad': edad
    }
    
    personas.append(persona)
    
    print("Datos de la persona guardados exitosamente.")


def buscar_persona(personas):
    nif = input("Ingrese el NIF de la persona a buscar: ")

    for persona in personas:
        if persona["NIF"] == nif:
            print("Información de la persona encontrada")
            print(f"Nombre: {persona['Nombre']}")
            print(f"Edad: {persona['Edad']}")
            return

    print("No se encontró ninguna persona con el NIF ingresado.")

def imprimir_certificados(personas):
    for persona in personas:
        print("Certificados de", persona['Nombre'])
        print("NIF:", persona['NIF'])
        print("Certificado de nacimiento: ENTREGADO")
        print("Certificado de estado conyugal: ENTREGADO")
        print("Certificado de pertenencia a la Unión Europea: ENTREGADO")
        print("------------------")

def menu():
    print("------ Menú ------")
    print("1. Ingresar datos")
    print("2. Buscar persona")
    print("3. Imprimir certificados")
    print("4. Salir")

personas = []

while True:
    menu()
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        grabar_persona(personas)
    elif opcion == "2":
        buscar_persona(personas)
    elif opcion == "3":
        imprimir_certificados(personas)
    elif opcion == "4":
        print("Gracias por usar el programa de ingreso,busqueda e impresion de certificados.")
        print("Autor: Fernando Muñoz")
        print("Versión: 1.0")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
