from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


def mostrar_menu():

    print("\n===== RESTAURANTE =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")


def main():

    usuario = Usuario(
        1,
        "Administrador",
        "admin@gmail.com"
    )

    restaurante = Restaurante()

    archivo_servicio = ArchivoServicio()

    restaurante.cargar_productos(
        archivo_servicio.cargar_productos()
    )

    print(f"\nBienvenido {usuario.nombre}")

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opción: "
        )

        if opcion == "1":

            try:

                codigo = input("Código: ")
                nombre = input("Nombre: ")
                precio = float(
                    input("Precio: ")
                )

                restaurante.agregar_producto(
                    codigo,
                    nombre,
                    precio
                )

                archivo_servicio.guardar_productos(
                    restaurante.listar_productos()
                )

            except ValueError as error:
                print(error)

        elif opcion == "2":

            productos = restaurante.listar_productos()

            if not productos:
                print("No hay productos.")
            else:
                for producto in productos:
                    print(producto)

        elif opcion == "3":

            codigo = input(
                "Código a buscar: "
            )

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto:
                print(producto)
            else:
                print(
                    "Producto no encontrado."
                )

        elif opcion == "4":

            try:

                codigo = input("Código: ")
                nombre = input(
                    "Nuevo nombre: "
                )
                precio = float(
                    input("Nuevo precio: ")
                )

                restaurante.actualizar_producto(
                    codigo,
                    nombre,
                    precio
                )

                archivo_servicio.guardar_productos(
                    restaurante.listar_productos()
                )

                print(
                    "Producto actualizado."
                )

            except ValueError as error:
                print(error)

        elif opcion == "5":

            try:

                codigo = input(
                    "Código a eliminar: "
                )

                restaurante.eliminar_producto(
                    codigo
                )

                archivo_servicio.guardar_productos(
                    restaurante.listar_productos()
                )

                print(
                    "Producto eliminado."
                )

            except ValueError as error:
                print(error)

        elif opcion == "6":

            print("Programa finalizado.")
            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    main()