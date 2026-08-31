class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")

        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")

        self.stock -= cantidad

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }