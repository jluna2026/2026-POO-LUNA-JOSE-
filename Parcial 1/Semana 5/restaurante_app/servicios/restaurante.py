from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self, nombre: str, abierto: bool):
        self.nombre = nombre              # str
        self.abierto = abierto            # bool
        self.productos = []               # list[Producto]
        self.clientes = []                # list[Cliente]

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto en la lista de productos."""
        if producto not in self.productos:
            self.productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente en la lista de clientes."""
        if cliente not in self.clientes:
            self.clientes.append(cliente)

    def abrir(self) -> None:
        """Marca el restaurante como abierto."""
        self.abierto = True

    def cerrar(self) -> None:
        """Marca el restaurante como cerrado."""
        self.abierto = False

    def listar_productos(self) -> str:
        """Devuelve un texto con todos los productos registrados."""
        if not self.productos:
            return "No hay productos registrados."
        return "\n".join(str(p) for p in self.productos)

    def listar_clientes(self) -> str:
        """Devuelve un texto con todos los clientes registrados."""
        if not self.clientes:
            return "No hay clientes registrados."
        return "\n".join(str(c) for c in self.clientes)

    def __str__(self) -> str:
        estado = "Abierto" if self.abierto else "Cerrado"
        return (
            f"Restaurante: {self.nombre} | Estado: {estado}\n"
            f"--- Productos ---\n{self.listar_productos()}\n"
            f"--- Clientes ---\n{self.listar_clientes()}"
        )
