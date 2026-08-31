from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

restaurante = Restaurante()

while True:

    print("\n===== RESTAURANTE =====")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Vender producto")
    print("4. Consultar ventas usuario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")

        usuario = Usuario(
            identificacion,
            nombre
        )

        restaurante.agregar_usuario(usuario)

        print("Usuario registrado")

    elif opcion == "2":

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        restaurante.agregar_producto(producto)

        print("Producto registrado")

    elif opcion == "3":

        usuario = input(
            "Identificación usuario: "
        )

        codigo = input(
            "Código producto: "
        )

        cantidad = int(
            input("Cantidad: ")
        )

        if restaurante.vender_producto(
                codigo,
                usuario,
                cantidad):

            print("Venta realizada")

        else:
            print("No fue posible realizar la venta")

    elif opcion == "4":

        identificacion = input(
            "Identificación usuario: "
        )

        ventas = restaurante.ventas_usuario(
            identificacion
        )

        for venta in ventas:

            print(
                f"Producto: {venta.producto_codigo}"
            )

            print(
                f"Cantidad: {venta.cantidad}"
            )

    elif opcion ==