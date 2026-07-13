class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self._precio = valor

    def mostrar_informacion(self):
        return f"{self._nombre} ({self._categoria}) - ${self._precio:.2f} | {'Disponible' if self._disponible else 'No disponible'}"
