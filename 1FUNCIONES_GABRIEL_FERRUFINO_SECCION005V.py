from PRINCIPAL_GABRIEL_FERRUFINO_SECCION005V import *

Basedatos = [
    {
        "nombre": "Juanito",
        "apellido": "Perez",
        "correo": "juanito@ejemplo.com",
        "ID": 1,
        "puntos acumulados": 450,
        "monto total": 45000
    }
]
#la bienvenida

print("¡Bienvenidos a nuestro supermercado TODOAHORRO!\n")

while True:
#opciones que puede usar1
    print("eliga una de las siguientes opciones:")
    print("1. Registrar cliente")
    print("2. Listar clientes registrados")
    print("3. Registra tus compras")
    print("4. Listar compras de clientes")
    print("5. Salir")

    opcion = input("\nIngrese la opción que prefiera: ")

    if opcion == "1":
        registrar_cliente(Basedatos)
    elif opcion == "2":
        listar_cliente(Basedatos)
    elif opcion == "3":
        registrar_compra(Basedatos)
    elif opcion == "4":
        listar_comprascliente(Basedatos)
    elif opcion == "5":
        print("\n¡Muchas gracias por preferirnos! Esperamos verte pronto en Supermercados TODOAHORRO!!")
        break
    else:
        print("\nesa opcion no existe, elige otra opción para ayudarte\n")