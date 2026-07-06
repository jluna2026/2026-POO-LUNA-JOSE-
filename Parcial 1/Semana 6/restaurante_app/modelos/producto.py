class Producto:
    def __init__(self, nombre, precio, disponible=True):
        self._nombre = nombre
        self._precio = precio
        self._disponible = disponible

    def obtener_precio(self):
        return self._precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("❌ El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        return f"{self._nombre} - ${self._precio:.2f} - {'Disponible' if self._disponible else 'No disponible'}"
