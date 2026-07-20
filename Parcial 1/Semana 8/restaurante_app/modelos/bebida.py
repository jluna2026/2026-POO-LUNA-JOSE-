# modelos/bebida.py
from .producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamaño: str):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño = tamaño

    def mostrar_informacion(self) -> str:
        return f"[{self.codigo}] {self.nombre} ({self.tamaño}) - {self.categoria} - ${self.precio:.2f}"
