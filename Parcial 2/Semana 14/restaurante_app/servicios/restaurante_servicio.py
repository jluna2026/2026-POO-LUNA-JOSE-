from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.productos_file = "restaurante_app/datos/productos.json"
        self.usuarios_file = "restaurante_app/datos/usuarios.json"

    # ---------------- USUARIOS ----------------
    def listar_usuarios(self):
        datos = ArchivoServicio.cargar(self.usuarios_file)
        return [Usuario(u["identificacion"], u["nombre"], u["password"]) for u in datos]

    def validar_usuario(self, identificacion, password):
        usuarios = self.listar_usuarios()
        for u in usuarios:
            if u.identificacion == identificacion and u.password == password:
                return True
        return False

    # ---------------- PRODUCTOS ----------------
    def listar_productos(self):
        datos = ArchivoServicio.cargar(self.productos_file)
        return [Producto(p["codigo"], p["nombre"], p["precio"], p["stock"]) for p in datos]

    def registrar_producto(self, codigo, nombre, precio, stock):
        productos = ArchivoServicio.cargar(self.productos_file)
        if any(p["codigo"] == codigo for p in productos):
            raise ValueError("El producto ya existe.")
        nuevo = {"codigo": codigo, "nombre": nombre, "precio": precio, "stock": stock}
        productos.append(nuevo)
        ArchivoServicio.guardar(self.productos_file, productos)

    def consultar_producto(self, codigo):
        productos = self.listar_productos()
        for p in productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo, nombre, precio, stock):
        productos = ArchivoServicio.cargar(self.productos_file)
        for p in productos:
            if p["codigo"] == codigo:
                p["nombre"] = nombre
                p["precio"] = precio
                p["stock"] = stock
                ArchivoServicio.guardar(self.productos_file, productos)
                return
        raise ValueError("Producto no encontrado.")

    def eliminar_producto(self, codigo):
        productos = ArchivoServicio.cargar(self.productos_file)
        productos = [p for p in productos if p["codigo"] != codigo]
        ArchivoServicio.guardar(self.productos_file, productos)
