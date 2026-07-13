
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def menu():
    restaurante = Restaurante()

    while True:
        print("\nSISTEMA DE RESTAURANTE")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Registrar cliente")
        print("5. Listar clientes")
        print("6. Buscar cliente")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            producto = Producto(nombre, categoria, precio)
            restaurante.registrar_producto(producto)
            print("✅ Producto registrado")

        elif opcion == "2":
            for info in restaurante.listar_productos():
                print(info)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            resultados = restaurante.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p.mostrar_informacion())
            else:
                print("❌ Producto no encontrado")

        elif opcion == "4":
            id_cliente = int(input("ID del cliente: "))
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            cliente = Cliente(id_cliente, nombre, correo)
            restaurante.registrar_cliente(cliente)
            print("✅ Cliente registrado")

        elif opcion == "5":
            for info in restaurante.listar_clientes():
                print(info)

        elif opcion == "6":
            id_cliente = int(input("ID a buscar: "))
            cliente = restaurante.buscar_cliente(id_cliente)
            print(cliente if cliente else "❌ Cliente no encontrado")

        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida")
