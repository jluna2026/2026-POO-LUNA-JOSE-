    import re

    class Usuario:
        def __init__(self, identificacion: str, nombre: str):
            if not re.fullmatch(r"\d{10}", identificacion):
                raise ValueError("Identificación inválida (debe tener 10 dígitos)")
            self.identificacion = identificacion
            self.nombre = nombre

        def to_dict(self):
            return {
                "identificacion": self.identificacion,
                "nombre": self.nombre
            }
