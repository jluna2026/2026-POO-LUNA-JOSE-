import json

from modelos.producto import Producto


class ArchivoServicio:

    def __init__(self):
        self.ruta_archivo = "datos/productos.json"

    def cargar_productos(self):

        try:

            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos = []

            for item in datos:
                producto = Producto.desde_diccionario(
                    item
                )
                productos.append(producto)

            return productos

        except FileNotFoundError:

            print("Archivo no encontrado.")
            return []

        except json.JSONDecodeError:

            print("Error en el JSON.")
            return []

    def guardar_productos(
        self,
        productos
    ):

        datos = []

        for producto in productos:
            datos.append(
                producto.a_diccionario()
            )

        with open(
            self.ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(
            "Productos guardados correctamente."
        )