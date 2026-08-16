from typing import List, Set, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """Servicio encargado de administrar las colecciones y reglas de negocio."""

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        # LISTAS: Colecciones dinámicas para almacenar objetos
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

    # --- OPERACIONES DE PRODUCTOS ---

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto evitando códigos duplicados."""
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self.productos.append(producto)
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca y retorna un producto por su código único."""
        for prod in self.productos:
            if prod.codigo.lower() == codigo.lower():
                return prod
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        """Actualiza los datos de un producto existente."""
        prod = self.buscar_producto_por_codigo(codigo)
        if prod:
            prod.nombre = nuevo_nombre
            prod.categoria = nueva_categoria
            prod.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código."""
        prod = self.buscar_producto_por_codigo(codigo)
        if prod:
            self.productos.remove(prod)
            return True
        return False

    def obtener_todos_los_productos(self) -> List[Producto]:
        """Retorna la lista completa de productos."""
        return self.productos

    # --- OPERACIONES CON CONJUNTOS (SET) ---

    def obtener_categorias_unicas(self) -> Set[str]:
        """CONJUNTO (set): Extrae las categorías únicas sin duplicados."""
        categorias: Set[str] = {prod.categoria for prod in self.productos}
        return categorias

    # --- OPERACIONES DE USUARIOS ---

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""
        if self.buscar_usuario_por_id(usuario.identificacion) is not None:
            return False
        self.usuarios.append(usuario)
        return True

    def buscar_usuario_por_id(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su número de identificación."""
        for usr in self.usuarios:
            if usr.identificacion.lower() == identificacion.lower():
                return usr
        return None

    def obtener_todos_los_usuarios(self) -> List[Usuario]:
        """Retorna la lista completa de usuarios."""
        return self.usuarios