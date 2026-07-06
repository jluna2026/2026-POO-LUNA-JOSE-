from .producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    def mostrar_informacion(self):
        return f"🍽️ Platillo: {self._nombre} | Precio: ${self._precio:.2f} | Calorías: {self.calorias}"
