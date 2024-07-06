def saludo():
    print("Bienvenidos al supermercado TODOAHORRO!!!")

def menu():
    opciones = [
        "1. Registrar cliente",
        "2. Listar clientes registrados",
        "3. Registrar compra",
        "4. Listar compras del cliente",
        "5. Salir",
    ]

    for i, opcion in enumerate(opciones):
        print(f"{opcion}")



#opcion 1
def registrar_cliente(Basedatos):
    nombre = input("ingrese su nombre: ").upper()
    apellido = input("Ingrese ingrese su apellido: ").upper()
    correo_electronico = input("ingrese su correo porfavor: ").upper()

    id_cliente = len(Basedatos) + 1

    Basedatos.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "correo" : correo_electronico,
            "ID": id_cliente,
            "puntos acumulados": []
        }
    )

    print("\n¡Cliente registrado exitosamente!\n")



#opcion 2
def listar_cliente(Basedatos):
    print("\nLos clientes registrados son:\n")
    print("Nombre\t\t\tID\t\t\tcorreo")
    for cliente in Basedatos:
        print(f'{cliente["nombre"]} {cliente["apellido"]}\t{cliente["ID"]}\t\t{cliente["correo"]}')

    print("\nla lista a sido creada existosamente!!!!!\n")



#opcion 3
def registrar_compra(id_usuario, fecha_compra, monto_compra):
    monto_compra = float(input("Ingrese el valor de su compra: "))
    puntos_acumulados = int(monto_compra * 0.01)
    fecha_compra =[]

    print(f"Compra del usuario con ID {id_usuario} el {fecha_compra}.")
    print(f"sus puntos acumulados son: {puntos_acumulados}")



#opcion 4

def listar_comprascliente(BaseDatos, id_usuario):
    cliente_encontrado = None
    for cliente in BaseDatos:
        if cliente.get("ID") == id_usuario:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        print("\nListado de compras del cliente:\n")
        print(f"Nombre: {cliente_encontrado['nombre']} {cliente_encontrado['apellido']}")
        print("Fecha de Compra\tMonto Total\tPuntos acumulados")

        compras = cliente_encontrado.get("compras", [])
        if compras:
            for compra in compras:
                fecha = compra.get("fecha", "")
                monto = compra.get("monto", "")
                puntos = compra.get("puntos", "")
                print(f"{fecha}\t{monto}\t{puntos}")

            nombre_archivo = f"RESUMEN_CLIENTE_ID_{id_usuario}.txt"
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(f"ID CLIENTE: {id_usuario}\n")
                archivo.write(f"NOMBRE CLIENTE: {cliente_encontrado['nombre']} {cliente_encontrado['apellido']}\n")
                archivo.write("Fecha de Compra\tMonto Total\tPuntos\n")
                for compra in compras:
                    fecha = compra.get("fecha", "")
                    monto = compra.get("monto", "")
                    puntos = compra.get("puntos", "")
                    archivo.write(f"{fecha}\t{monto}\t{puntos}\n")
                puntos_totales = sum(compra.get("puntos", 0) for compra in compras)
                archivo.write(f"PUNTOS TOTALES A CANJEAR: {puntos_totales} pesos\n")

            print(f"\nSe ha creado el archivo '{nombre_archivo}' con el resumen de compras del cliente.")


if __name__ == "__main__":
    Basedatos = []

    saludo()

    while True:
        menu()
        opcion = input("\nIngresa la opcion que prefieras: ")

        if opcion == "1":
            registrar_cliente(Basedatos)
        elif opcion == "2":
            listar_cliente(Basedatos)
        elif opcion == "3":
            id_usuario = input("Ingrese el ID del cliente: ")
            fecha_compra = input("Ingrese la fecha de la compra: ")
            registrar_compra(id_usuario, fecha_compra, Basedatos)
        elif opcion == "4":
            listar_comprascliente(Basedatos)
        elif opcion == "5":
            print("¡MUCHAS GRACIAS POR PREFERIRNOS VUELVE PRONTO!")
            break
        else:
            print("cueek se equivoco eliga una opcion de la 1 a la 5 no es tan dificil xd.")


