# main.py
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def menu():
    restaurante = Restaurante()
    while True:
        print("\n***************************************")
        print("SISTEMA DE RESTAURANTE")
        print("***************************************")
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("---------------------------------------")
        print("4. Listar productos")
        print("5. Listar clientes")
        print("---------------------------------------")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            restaurante.registrar_producto(Producto(codigo, nombre, categoria, precio))

        elif opcion == "2":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            tamaño = input("Tamaño: ")
            restaurante.registrar_producto(Bebida(codigo, nombre, categoria, precio, tamaño))

        elif opcion == "3":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            restaurante.registrar_cliente(Cliente(identificacion, nombre, correo))

        elif opcion == "4":
            restaurante.listar_productos()

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    menu()
