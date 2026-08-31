class Usuario:
    def __init__(self, identificacion: str, nombre: str):
        self.identificacion = identificacion
        self.nombre = nombre

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre
        }