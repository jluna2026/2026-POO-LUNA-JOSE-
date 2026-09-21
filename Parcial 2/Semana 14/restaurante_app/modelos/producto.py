class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        # Validaciones básicas
        if not codigo:
            raise ValueError("El código no puede estar vacío")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int):
        """Reduce el stock al vender cierta cantidad."""
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def to_dict(self):
        """Convierte el objeto Producto en un diccionario (para guardar en JSON)."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}, Precio: {self.precio}, Stock: {self.stock})"
