from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    # Productos
    def registrar_producto(self, producto: Producto):
        self.productos.append(producto)

    def listar_productos(self):
        return [p.mostrar_informacion() for p in self.productos]

    def buscar_producto(self, nombre: str):
        return [p for p in self.productos if p.nombre.lower() == nombre.lower()]

    # Clientes
    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return [f"{c.id_cliente} - {c.nombre} ({c.correo})" for c in self.clientes]

    def buscar_cliente(self, id_cliente: int):
        return next((c for c in self.clientes if c.id_cliente == id_cliente), None)
