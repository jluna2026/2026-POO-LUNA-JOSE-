# Este archivo convierte la carpeta 'servicios' en un paquete.
# Se importa la clase Restaurante para que esté disponible al usar el paquete.

from .restaurante import Restaurante

__all__ = ["Restaurante"]
