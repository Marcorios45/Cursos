agenda = []

def agregar_contacto(nombre, telefono, email):
    contacto = {
        "Nombre": nombre,
        "Telefono": telefono,
        "Email": email
    }

    agenda.append(contacto)
    print("~~Contacto agregado con exito.~~")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto['Nombre'] == nombre:
            print("CONTACTO ENCONTRADO EXITOSAMENTE:")
            for clave,valor in contacto.items():
                print(f"{clave}: {valor}")
            return
    print("Contacto no encontrado.")

def mostrar_contactos():
    if len(agenda)>0:
        print("Lista de contactos: ")
        for contacto in agenda:
            print("\n".join(f"{clave}: {valor}" for clave, valor in contacto.items()))
    else:
        print("La agenda se ecuentra vacia, agregue contactos.")

def eliminar_contacto(contacto_delate):
    for contacto in agenda:
        if contacto['Nombre'] == contacto_delate:
            agenda.remove(contacto)
            print("Contacto eliminado")
            return
        print("Contacto no encontrado.")

def main():
    while True:
        print("**********Agenda de contactos************")
        opcion = input("Ingresa una opción"
                       "\n1.Agregar contactos"
                       "\n2.Buscar contactos"
                       "\n3.Mostrar contactos"
                       "\n4.Eliminar contactos"
                       "\nPresione 'S' para salir.\n")
                
        if opcion.upper() == 'S':
            break
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = int(input("Ingrese el telefono del contacto: "))
                email = input("Ingrese el email del contacto: ")
                agregar_contacto(nombre,telefono,email)
            elif opcion == 2:
                nombre = input("Ingrese el nombre de su contacto: ")
                buscar_contacto(nombre)
            elif opcion == 3:
                mostrar_contactos()
            elif opcion == 4:
                contacto_delate = input("Ingrese el nombre del contacto a eliminar: ")
                eliminar_contacto(contacto_delate)
            else:
                print("Ingrese una opcion valida.")    
        else:
            print("Ingrese una opcion valida.")

if __name__ == "__main__":
    main()

