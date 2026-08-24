class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser un número mayor a cero.")

        self.id_producto = int(id_producto)
        self.nombre = nombre.strip()
        self.precio = float(precio)

    def to_dict(self) -> dict:
        """Convierte el objeto Producto a un diccionario compatible con JSON."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Reconstruye un objeto Producto a partir de un diccionario."""
        try:
            return cls(
                id_producto=data["id_producto"],
                nombre=data["nombre"],
                precio=data["precio"]
            )
        except (KeyError, TypeError, ValueError) as e:
            raise ValueError(f"Datos inválidos para reconstruir el Producto: {e}")

    def __str__(self):
        return f"ID: {self.id_producto} | {self.nombre} - ${self.precio:.2f}"
