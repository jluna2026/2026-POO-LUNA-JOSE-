from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self, productos=None, usuarios=None):
        # Archivos de persistencia
        self.productos_file = "restaurante_app/datos/productos.json"
        self.usuarios_file = "restaurante_app/datos/usuarios.json"

        # Si se pasan datos iniciales, se usan; si no, se cargan desde JSON
        self._productos = productos if productos is not None else ArchivoServicio.cargar(self.productos_file)
        self._usuarios = usuarios if usuarios is not None else ArchivoServicio.cargar(self.usuarios_file)

    # ---------------- USUARIOS ----------------
    def listar_usuarios(self):
        return [Usuario(u["identificacion"], u["nombre"], u["password"]) for u in self._usuarios]

    def validar_usuario(self, identificacion, password):
        for u in self._usuarios:
            if u["identificacion"] == identificacion and u["password"] == password:
                return True
        return False
    # ---------------- PRODUCTOS ----------------
    def listar_productos(self):
        return [Producto(p["codigo"], p["nombre"], p["precio"], p["stock"]) for p in self._productos]

    def registrar_producto(self, codigo, nombre, precio, stock):
        # Validaciones de negocio
        if any(p["codigo"] == codigo for p in self._productos):
            raise ValueError("El producto ya existe.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        nuevo = {"codigo": codigo, "nombre": nombre, "precio": precio, "stock": stock}
        self._productos.append(nuevo)
        ArchivoServicio.guardar(self.productos_file, self._productos)

    def consultar_producto(self, codigo):
        for p in self._productos:
            if p["codigo"] == codigo:
                return Producto(p["codigo"], p["nombre"], p["precio"], p["stock"])
        return None

    def actualizar_producto(self, codigo, nombre, precio, stock):
        for p in self._productos:
            if p["codigo"] == codigo:
                p["nombre"] = nombre
                p["precio"] = precio
                p["stock"] = stock
                ArchivoServicio.guardar(self.productos_file, self._productos)
                return
        raise ValueError("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        inicial = len(self._productos)
        self._productos = [p for p in self._productos if p["codigo"] != codigo]
        if len(self._productos) == inicial:
            raise ValueError("Producto no encontrado.")
        ArchivoServicio.guardar(self.productos_file, self._productos)
