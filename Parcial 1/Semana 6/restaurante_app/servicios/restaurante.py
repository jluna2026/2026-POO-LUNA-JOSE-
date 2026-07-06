class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_menu(self):
        print(f"\n📋 Menú del restaurante {self.nombre}:")
        for producto in self.productos:
            print(producto.mostrar_informacion())
