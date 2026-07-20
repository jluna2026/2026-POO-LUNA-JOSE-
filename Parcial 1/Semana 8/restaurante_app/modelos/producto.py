# modelos/producto.py
class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.categoria} - ${self.precio:.2f}"
