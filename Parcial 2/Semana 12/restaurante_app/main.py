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
    print("5. Listar productos por stock")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        identificacion = input("Identificación (10 dígitos): ")
        nombre = input("Nombre: ")
        try:
            usuario = Usuario(identificacion, nombre)
            restaurante.agregar_usuario(usuario)
            print("✅ Usuario registrado")
        except ValueError as e:
            print("⚠️", e)

    elif opcion == "2":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto = Producto(codigo, nombre, precio, stock)
            restaurante.agregar_producto(producto)
            print("✅ Producto registrado")
        except ValueError as e:
            print("⚠️", e)

    elif opcion == "3":
        usuario = input("Identificación usuario: ")
        codigo = input("Código producto: ")
        cantidad = int(input("Cantidad: "))
        if restaurante.vender_producto(codigo, usuario, cantidad):
            print("✅ Venta realizada")
        else:
            print("⚠️ No fue posible realizar la venta")

    elif opcion == "4":
        identificacion = input("Identificación usuario: ")
        ventas = restaurante.ventas_usuario(identificacion)
        if ventas:
            for v in ventas:
                print(f"Producto: {v.producto_codigo} | Cantidad: {v.cantidad} | Fecha: {v.fecha}")
        else:
            print("⚠️ No hay ventas registradas para este usuario")

    elif opcion == "5":
        productos = restaurante.productos_ordenados_por_stock()
        for p in productos:
            print(f"{p.codigo} - {p.nombre} | Stock: {p.stock}")

    elif opcion == "6":
        print("👋 Programa finalizado")
        break

    else:
        print("⚠️ Opción inválida")
