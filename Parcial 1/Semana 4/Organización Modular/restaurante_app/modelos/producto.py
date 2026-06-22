# modelos/producto.py
# -------------------------------------------------------------
# Módulo del MODELO "Producto".
# Su única responsabilidad es representar un producto del
# restaurante (plato, bebida, postre, etc.).
# -------------------------------------------------------------


class Producto:
    """Representa un producto disponible en el restaurante."""

    # Constructor: se ejecuta al crear cada objeto Producto
    def __init__(self, codigo, nombre, categoria, precio, disponible=True):
        self.codigo = codigo            # Identificador único del producto
        self.nombre = nombre            # Nombre del plato o bebida
        self.categoria = categoria      # Entrada, plato fuerte, bebida, postre...
        self.precio = precio            # Precio unitario en dólares
        self.disponible = disponible    # True si el producto está disponible

    # Método que gestiona la información: cambia la disponibilidad
    def cambiar_disponibilidad(self, estado):
        """Activa (True) o desactiva (False) la disponibilidad del producto."""
        self.disponible = estado

    # Método especial: define cómo se muestra el objeto como texto
    def __str__(self):
        estado = "Disponible" if self.disponible else "Agotado"
        return (f"[{self.codigo}] {self.nombre} ({self.categoria}) - "
                f"${self.precio:.2f} | {estado}")
