class Cliente:
    def __init__(self, nombre: str, edad: int, es_vip: bool):
        self.nombre = nombre      # str
        self.edad = edad          # int
        self.es_vip = es_vip      # bool

    def activar_vip(self) -> None:
        """Convierte al cliente en VIP."""
        self.es_vip = True

    def desactivar_vip(self) -> None:
        """Quita el estado VIP al cliente."""
        self.es_vip = False

    def __str__(self) -> str:
        estado_vip = "VIP" if self.es_vip else "Regular"
        return f"Cliente: {self.nombre} | Edad: {self.edad} | Tipo: {estado_vip}"
