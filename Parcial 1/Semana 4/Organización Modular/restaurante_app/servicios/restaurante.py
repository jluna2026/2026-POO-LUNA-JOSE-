# servicios/restaurante.py
# -------------------------------------------------------------
# Módulo del SERVICIO "Restaurante".
# Su responsabilidad es coordinar las operaciones del sistema:
# administra los productos y clientes registrados.
# -------------------------------------------------------------


class Restaurante:
    """Administra los productos y clientes registrados en el sistema."""

    # Constructor del servicio principal
    def __init__(self, nombre):
        self.nombre = nombre        # Nombre del restaurante
        self.productos = []         # Lista que almacena objetos Producto
        self.clientes = []          # Lista que almacena objetos Cliente

    # ---------------- Gestión de productos ----------------
    def agregar_producto(self, producto):
        """Agrega un objeto Producto a la lista del restaurante."""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra en consola todos los productos registrados."""
        print(f"\n--- MENÚ de {self.nombre} ---")
        if not self.productos:
            print("No hay productos registrados.")
        for producto in self.productos:
            print(producto)   # Aquí se usa el método __str__ de Producto

    # ---------------- Gestión de clientes ----------------
    def agregar_cliente(self, cliente):
        """Agrega un objeto Cliente a la lista del restaurante."""
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        """Muestra en consola todos los clientes registrados."""
        print(f"\n--- CLIENTES de {self.nombre} ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        for cliente in self.clientes:
            print(cliente)     # Aquí se usa el método __str__ de Cliente

    # ---------------- Consultas adicionales ----------------
    def buscar_producto(self, codigo):
        """Busca un producto por su código y lo devuelve si existe."""
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None  # Si no se encuentra, devuelve None

    def total_menu(self):
        """Suma el precio de todos los productos disponibles."""
        return sum(p.precio for p in self.productos if p.disponible)
