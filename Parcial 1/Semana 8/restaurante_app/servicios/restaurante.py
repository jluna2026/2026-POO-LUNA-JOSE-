# servicios/restaurante.py
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente: Cliente):
        if any(c.identificacion == cliente.identificacion for c in self.clientes):
            print("⚠️ Cliente ya registrado.")
        else:
            self.clientes.append(cliente)

    def listar_productos(self):
        for p in self.productos:
            print(p.mostrar_informacion())

    def listar_clientes(self):
        for c in self.clientes:
            print(c.mostrar_informacion())
