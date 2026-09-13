from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.libros = []
        self.cargar_datos()

    def cargar_datos(self):
        # Carga los datos persistidos y los convierte en objetos.
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        libros_json = self.archivo_servicio.leer_json("libros.json")

        self.usuarios = [
            Usuario(
                datos.get("identificador", ""),
                datos.get("nombre", ""),
                datos.get("usuario", ""),
                datos.get("contraseña", datos.get("contrasena", "")),
            )
            for datos in usuarios_json
        ]

        self.libros = [
            Libro(
                datos.get("codigo", ""),
                datos.get("titulo", ""),
                datos.get("autor", ""),
            )
            for datos in libros_json
        ]

    def validar_acceso(self, usuario, contrasena):
        # Verifica si las credenciales coinciden con un usuario cargado.
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado

        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_libros(self):
        return len(self.libros)

    def listar_usuarios(self):
        # Entrega los usuarios cargados para mostrarlos en la interfaz.
        return self.usuarios

    def listar_libros(self):
        # Entrega los libros cargados para mostrarlos en la interfaz.
        return self.libros
