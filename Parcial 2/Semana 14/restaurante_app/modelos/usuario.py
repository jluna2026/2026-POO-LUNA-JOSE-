class Usuario:
    def __init__(self, identificacion: str, nombre: str, password: str):
        # Validaciones básicas
        if not identificacion.isdigit():
            raise ValueError("La identificación debe ser numérica")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not password:
            raise ValueError("La contraseña no puede estar vacía")

        self.identificacion = identificacion
        self.nombre = nombre
        self.password = password

    def to_dict(self):
        """Convierte el objeto Usuario en un diccionario (para guardar en JSON)."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "password": self.password
        }

    def __str__(self):
        return f"Usuario {self.nombre} (ID: {self.identificacion})"
