class Usuario:

    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} - {self.correo}"