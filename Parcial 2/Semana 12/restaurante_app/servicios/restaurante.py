from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self._productos = []
        self._usuarios = []
        self._ventas = []
        self._productos_dict = {}
        self._usuarios_dict = {}
        self.cargar_datos()

    def cargar_datos(self):
        productos = ArchivoServicio.cargar("datos/productos.json")
        usuarios = ArchivoServicio.cargar("datos/usuarios.json")
        ventas = ArchivoServicio.cargar("datos/ventas.json")

        self._productos = [Producto(**p) for p in productos]
        self._usuarios = [Usuario(**u) for u in usuarios]
        self._ventas = [Venta(**v) for v in ventas]

        self._productos_dict = {p.codigo: p for p in self._productos}
        self._usuarios_dict = {u.identificacion: u for u in self._usuarios}

    def guardar_productos(self):
        ArchivoServicio.guardar("datos/productos.json", [p.to_dict() for p in self._productos])

    def guardar_usuarios(self):
        ArchivoServicio.guardar("datos/usuarios.json", [u.to_dict() for u in self._usuarios])

    def guardar_ventas(self):
        ArchivoServicio.guardar("datos/ventas.json", [v.to_dict() for v in self._ventas])

    def agregar_producto(self, producto: Producto):
        if producto.codigo in self._productos_dict:
            print("⚠️ Producto ya registrado")
            return
        self._productos.append(producto)
        self._productos_dict[producto.codigo] = producto
        self.guardar_productos()

    def agregar_usuario(self, usuario: Usuario):
        if usuario.identificacion in self._usuarios_dict:
            print("⚠️ Usuario ya registrado")
            return
        self._usuarios.append(usuario)
        self._usuarios_dict[usuario.identificacion] = usuario
        self.guardar_usuarios()

    def buscar_producto(self, codigo: str):
        return self._productos_dict.get(codigo)

    def buscar_usuario(self, identificacion: str):
        return self._usuarios_dict.get(identificacion)

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int):
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None or cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)

        self.guardar_ventas()
        self.guardar_productos()
        return True

    def ventas_usuario(self, identificacion: str):
        return [v for v in self._ventas if v.usuario_id == identificacion]

    def productos_ordenados_por_stock(self):
        # Devuelve productos ordenados de mayor a menor stock
        return sorted(self._productos, key=lambda p: p.stock, reverse=True)
