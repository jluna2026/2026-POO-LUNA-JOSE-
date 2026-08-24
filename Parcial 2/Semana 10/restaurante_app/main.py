from servicios.restaurante import RestauranteService


def menu():
    print("\n--- APP RESTAURANTE (PERSISTENCIA JSON) ---")
    print("1. Listar Productos")
    print("2. Registrar Producto")
    print("3. Eliminar Producto")
    print("4. Salir")
    return input("Seleccione una opción: ")


def main():
    servicio = RestauranteService()

    while True:
        opcion = menu()

        if opcion == "1":
            productos = servicio.listar_productos()
            if not productos:
                print("\nNo hay productos registrados en el sistema.")
            else:
                print("\n--- Lista de Productos ---")
                for p in productos:
                    print(p)

        elif opcion == "2":
            try:
                id_prod = int(input("Ingrese ID del producto (Entero): "))
                nombre = input("Ingrese nombre del producto: ")
                precio = float(input("Ingrese precio del producto: "))

                resultado = servicio.registrar_producto(id_prod, nombre, precio)
                print(f"\n{resultado}")
            except ValueError:
                print("\n[Error] El ID debe ser entero y el precio un valor numérico.")

        elif opcion == "3":
            try:
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                resultado = servicio.eliminar_producto(id_prod)
                print(f"\n{resultado}")
            except ValueError:
                print("\n[Error] El ID debe ser un número entero.")

        elif opcion == "4":
            print("\nCerrando aplicación. ¡Datos guardados correctamente!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
