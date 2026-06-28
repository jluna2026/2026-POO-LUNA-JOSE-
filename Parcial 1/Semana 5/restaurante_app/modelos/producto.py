class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre          # str
        self.precio = precio          # float
        self.disponible = disponible  # bool

    def aplicar_descuento(self, porcentaje: float) -> None:
        """Aplica un descuento al precio del producto."""
        if porcentaje > 0:
            self.precio = self.precio * (1 - porcentaje / 100)

    def marcar_no_disponible(self) -> None:
        """Marca el producto como no disponible."""
        self.disponible = False

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado}"
