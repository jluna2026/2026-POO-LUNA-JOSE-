from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def crear_productos_generales():
    """Crea productos generales del restaurante."""
    p1 = Producto("Hamburguesa clásica", 5.50, True)
    p2 = Producto("Pizza margarita", 7.25, True)
    return [p1, p2]


def crear_clientes():
    """Crea clientes registrados."""
    c1 = Cliente("Ana Pérez", 25, True)
    c2 = Cliente("Luis Gómez", 32, False)
    return [c1, c2]


def main():
    # Crear restaurante
    restaurante = Restaurante("La Buena Mesa", abierto=True)

    # Registrar productos generales
    for producto in crear_productos_generales():
        restaurante.registrar_producto(producto)

    # Registrar clientes
    for cliente in crear_clientes():
        restaurante.registrar_cliente(cliente)

    # Mostrar información completa del restaurante
    print(restaurante)


if __name__ == "__main__":
    main()
