from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):

        self._productos = []
        self._usuarios = []
        self._ventas = []

        self.cargar_datos()

    def cargar_datos(self):

        productos = ArchivoServicio.cargar(
            "datos/productos.json"
        )

        usuarios = ArchivoServicio.cargar(
            "datos/usuarios.json"
        )

        ventas = ArchivoServicio.cargar(
            "datos/ventas.json"
        )

        self._productos = [
            Producto(
                p["codigo"],
                p["nombre"],
                p["precio"],
                p["stock"]
            )
            for p in productos
        ]

        self._usuarios = [
            Usuario(
                u["identificacion"],
                u["nombre"]
            )
            for u in usuarios
        ]

        self._ventas = [
            Venta(
                v["usuario_id"],
                v["producto_codigo"],
                v["cantidad"]
            )
            for v in ventas
        ]

    def guardar_productos(self):
        ArchivoServicio.guardar(
            "datos/productos.json",
            [p.to_dict() for p in self._productos]
        )

    def guardar_usuarios(self):
        ArchivoServicio.guardar(
            "datos/usuarios.json",
            [u.to_dict() for u in self._usuarios]
        )

    def guardar_ventas(self):
        ArchivoServicio.guardar(
            "datos/ventas.json",
            [v.to_dict() for v in self._ventas]
        )

    def agregar_producto(self, producto):
        self._productos.append(producto)
        self.guardar_productos()

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)
        self.guardar_usuarios()

    def buscar_producto(self, codigo):

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def buscar_usuario(self, identificacion):

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def vender_producto(
        self,
        codigo_producto,
        identificacion_usuario,
        cantidad
    ):

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None or producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        self.guardar_ventas()
        self.guardar_productos()

        return True

    def ventas_usuario(self, identificacion):

        resultado = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion:
                resultado.append(venta)

        return resultado