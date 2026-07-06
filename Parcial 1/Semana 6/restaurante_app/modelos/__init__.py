# Este archivo convierte la carpeta 'modelos' en un paquete.
# Aquí se importan las clases principales para facilitar su uso.

from .producto import Producto
from .platillo import Platillo
from .bebida import Bebida

__all__ = ["Producto", "Platillo", "Bebida"]
