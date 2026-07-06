from .producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, mililitros, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.mililitros = mililitros

    def mostrar_informacion(self):
        return f"🥤 Bebida: {self._nombre} | Precio: ${self._precio:.2f} | Tamaño: {self.mililitros} ml"
