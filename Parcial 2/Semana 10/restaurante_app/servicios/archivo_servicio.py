import json
import os

from modelos.producto import Producto


class ArchivoServicio:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

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

                    productos.append(
                        Producto.desde_diccionario(
                            item
                        )
                    )

                return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            return []

    def guardar_productos(self, productos):

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

        print("Productos guardados correctamente.")


        