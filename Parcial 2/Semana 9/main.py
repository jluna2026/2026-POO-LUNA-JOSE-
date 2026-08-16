from typing import Tuple, Dict, Callable
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# TUPLA: Información inmutable de las opciones del menú principal
OPCIONES_MENU: Tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir"
)


def ejecutar_registrar_producto(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Ingrese código único del producto: ").strip()
    if servicio.buscar_producto_por_codigo(codigo):
        print(" Error: Ya existe un producto con ese código.")
        return
    nombre = input("Ingrese nombre del producto: ").strip()
    categoria = input("Ingrese categoría: ").strip()
    try:
        precio = float(input("Ingrese precio: "))
        if precio < 0:
            print(" Error: El precio no puede ser negativo.")
            return
    except ValueError:
        print(" Error: Debe ingresar un valor numérico válido para el precio.")
        return

    nuevo_producto = Producto(codigo, nombre, categoria, precio)
    if servicio.registrar_producto(nuevo_producto):
        print(" Producto registrado con éxito.")


def ejecutar_buscar_producto(servicio: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    prod = servicio.buscar_producto_por_codigo(codigo)
    if prod:
        print(f"Producto encontrado: {prod}")
    else:
        print(" No se encontró ningún producto con ese código.")


def ejecutar_actualizar_producto(servicio: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    if not servicio.buscar_producto_por_codigo(codigo):
        print(" Error: El producto no existe.")
        return

    nuevo_nombre = input("Ingrese nuevo nombre: ").strip()
    nueva_cat = input("Ingrese nueva categoría: ").strip()
    try:
        nuevo_precio = float(input("Ingrese nuevo precio: "))
    except ValueError:
        print(" Error: Precio inválido.")
        return

    if servicio.actualizar_producto(codigo, nuevo_nombre, nueva_cat, nuevo_precio):
        print(" Producto actualizado exitosamente.")


def ejecutar_eliminar_producto(servicio: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if servicio.eliminar_producto(codigo):
        print(" Producto eliminado correctamente.")
    else:
        print(" Error: No existe un producto con ese código.")


def ejecutar_listar_productos(servicio: Restaurante) -> None:
    print("\n--- LISTA DE PRODUCTOS ---")
    productos = servicio.obtener_todos_los_productos()
    if not productos:
        print("No hay productos registrados.")
    else:
        for prod in productos:
            print(prod)


def ejecutar_registrar_usuario(servicio: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")
    id_user = input("Ingrese identificación/Cédula: ").strip()
    if servicio.buscar_usuario_por_id(id_user):
        print(" Error: Ya existe un usuario registrado con esa identificación.")
        return
    nombre = input("Ingrese nombre completo: ").strip()
    correo = input("Ingrese correo electrónico: ").strip()

    nuevo_usuario = Usuario(id_user, nombre, correo)
    if servicio.registrar_usuario(nuevo_usuario):
        print(" Usuario registrado exitosamente.")


def ejecutar_listar_usuarios(servicio: Restaurante) -> None:
    print("\n--- LISTA DE USUARIOS ---")
    usuarios = servicio.obtener_todos_los_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usr in usuarios:
            print(usr)


def ejecutar_mostrar_categorias(servicio: Restaurante) -> None:
    print("\n--- CATEGORÍAS ÚNICAS ---")
    categorias = servicio.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas aún.")
    else:
        for cat in categorias:
            print(f"- {cat}")


def main() -> None:
    servicio_restaurante = Restaurante("Gourmet Express")

    # DICCIONARIO: Mapeo de opción elegida (clave) a función ejecutable (valor)
    acciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": ejecutar_registrar_producto,
        "2": ejecutar_buscar_producto,
        "3": ejecutar_actualizar_producto,
        "4": ejecutar_eliminar_producto,
        "5": ejecutar_listar_productos,
        "6": ejecutar_registrar_usuario,
        "7": ejecutar_listar_usuarios,
        "8": ejecutar_mostrar_categorias
    }

    mantenimiento = True
    while mantenimiento:
        print("\n" + "=" * 35)
        print("     SISTEMA DE RESTAURANTE     ")
        print("=" * 35)

        # Recorrido iterativo de la TUPLA
        for opcion in OPCIONES_MENU:
            print(opcion)
        print("-" * 35)

        eleccion = input("Seleccione una opción (1-9): ").strip()

        if eleccion == "9":
            print("\n¡Gracias por utilizar el sistema!")
            mantenimiento = False
        elif eleccion in acciones:
            # Ejecución de la función despachada mediante el DICCIONARIO
            acciones[eleccion](servicio_restaurante)
        else:
            print(" Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()