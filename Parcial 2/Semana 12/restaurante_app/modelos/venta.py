from datetime import datetime

class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int, fecha: str = None):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida")
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        # Si no se pasa fecha, se asigna la actual
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }
