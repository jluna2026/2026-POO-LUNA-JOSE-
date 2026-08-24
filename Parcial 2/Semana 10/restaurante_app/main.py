from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

RUTA_ARCHIVO = "datos/productos.json"


def menu():

    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Listar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")


def main():

    restaurante = Restaurante()

    archivo_servicio = ArchivoServicio(
        RUTA_ARCHIVO
    )

    restaurante.cargar_productos(
        archivo_servicio.cargar_productos()
    )

    while True:

        menu()

        opcion = input("Opción: ")

        if opcion == "1":

            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))

            restaurante.agregar_producto(
                codigo,
                nombre,
                precio
            )

            archivo_servicio.guardar_productos(
                restaurante.listar_productos()
            )

        elif opcion == "2":

            productos = restaurante.listar_productos()

            if not productos:
                print("No hay productos.")

            for producto in productos:
                print(producto)

        elif opcion == "3":

            codigo = input("Código: ")
            nombre = input("Nuevo nombre: ")
            precio = float(
                input("Nuevo precio: ")
            )

            if restaurante.actualizar_producto(
                codigo,
                nombre,
                precio
            ):

                archivo_servicio.guardar_productos(
                    restaurante.listar_productos()
                )

                print("Actualizado.")

            else:
                print("No encontrado.")

        elif opcion == "4":

            codigo = input("Código: ")

            if restaurante.eliminar_producto(
                codigo
            ):

                archivo_servicio.guardar_productos(
                    restaurante.listar_productos()
                )

                print("Eliminado.")

            else:
                print("No encontrado.")

        elif opcion == "5":

            print("Fin del programa.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()