from modelos.producto import Producto
from servicios.archivo_servicio import cargar_productos, guardar_productos


class RestauranteService:
    def __init__(self):
        self.productos = []
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        """Recupera los registros al iniciar la aplicación."""
        datos = cargar_productos()
        for item in datos:
            try:
                # Reconstruye objetos Producto a partir de registros válidos
                producto = Producto.from_dict(item)
                self.productos.append(producto)
            except ValueError as e:
                print(f"[Aviso] Registro omitido por error de validación: {e}")

    def _sincronizar_archivo(self):
        """Guarda nuevamente la colección tras modificarla."""
        lista_dicts = [p.to_dict() for p in self.productos]
        guardar_productos(lista_dicts)

    def registrar_producto(self, id_producto: int, nombre: str, precio: float) -> str:
        """Crea y registra un nuevo producto de forma controlada."""
        # Verificar duplicados
        if any(p.id_producto == id_producto for p in self.productos):
            return "[Error] Ya existe un producto con ese ID."

        try:
            nuevo_prod = Producto(id_producto, nombre, precio)
            self.productos.append(nuevo_prod)
            self._sincronizar_archivo()
            return f"Producto '{nombre}' registrado exitosamente."
        except ValueError as e:
            return f"[ValueError] No se pudo registrar: {e}"

    def eliminar_producto(self, id_producto: int) -> str:
        """Elimina un producto por su ID."""
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                self._sincronizar_archivo()
                return "Producto eliminado exitosamente."
        return "[Error] Producto no encontrado."

    def listar_productos(self):
        """Retorna la lista de objetos Producto en el sistema."""
        return self.productos
