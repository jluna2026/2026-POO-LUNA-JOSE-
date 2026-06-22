# modelos/cliente.py
# -------------------------------------------------------------
# Módulo del MODELO "Cliente".
# Su única responsabilidad es representar a una persona que
# realiza o consume un pedido en el restaurante.
# -------------------------------------------------------------


class Cliente:
    """Representa a un cliente del restaurante."""

    # Constructor: se ejecuta al crear cada objeto Cliente
    def __init__(self, cedula, nombre, telefono, correo):
        self.cedula = cedula        # Documento de identidad del cliente
        self.nombre = nombre        # Nombre completo del cliente
        self.telefono = telefono    # Número de contacto
        self.correo = correo        # Correo electrónico

    # Método que gestiona la información: actualiza datos de contacto
    def actualizar_contacto(self, telefono, correo):
        """Permite modificar el teléfono y el correo del cliente."""
        self.telefono = telefono
        self.correo = correo

    # Método especial: define cómo se muestra el objeto como texto
    def __str__(self):
        return (f"{self.nombre} | Cédula: {self.cedula} | "
                f"Tel: {self.telefono} | Correo: {self.correo}")
