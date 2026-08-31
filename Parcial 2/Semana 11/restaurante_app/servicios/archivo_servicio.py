import json

class ArchivoServicio:

    @staticmethod
    def guardar(nombre_archivo, datos):
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

        except PermissionError:
            print("Error de permisos al guardar.")

    @staticmethod
    def cargar(nombre_archivo):

        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("JSON inválido")
            return []
        