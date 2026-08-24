from modelos.producto import Producto


class Restaurante:

    def __init__(self):
        self.productos = []

    def cargar_productos(self, productos):
        self.productos = productos

    def agregar_producto(self, codigo, nombre, precio):

        if self.buscar_producto(codigo):
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        producto = Producto(
            codigo,
            nombre,
            precio
        )

        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, codigo):

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo,
        nombre,
        precio
    ):

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado."
            )

        producto.nombre = nombre
        producto.precio = precio

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado."
            )

        self.productos.remove(producto)