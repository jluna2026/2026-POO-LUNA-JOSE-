from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:

    def __init__(self, productos_data, usuarios_data):

        self.productos = [
            Producto(p["id"], p["nombre"], p["cantidad"])
            for p in productos_data
        ]

        self.usuarios = [
            Usuario(u["usuario"], u["password"])
            for u in usuarios_data
        ]

    def validar_usuario(self, usuario, password):

        for u in self.usuarios:
            if u.usuario == usuario and u.password == password:
                return True

        return False

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios