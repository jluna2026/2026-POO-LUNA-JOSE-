import os
import json

RUTA_ARCHIVO = os.path.join("datos", "productos.json")


def guardar_productos(productos_dict_list: list) -> bool:
    """Guarda la lista de diccionarios de productos en el archivo JSON."""
    try:
        # Asegura que la carpeta 'datos' exista
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)

        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(productos_dict_list, archivo, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"\n[Error de Archivo] No se pudo escribir en el disco: {e}")
        return False


def cargar_productos() -> list:
    """Lee el archivo JSON y retorna la lista de datos cargados."""
    if not os.path.exists(RUTA_ARCHIVO):
        # La ausencia inicial del archivo no debe impedir ejecutar el programa
        return []

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("\n[Error de Formato] El archivo 'productos.json' está corrupto o es inválido.")
        return []
    except IOError as e:
        print(f"\n[Error de Archivo] No se pudo leer el archivo: {e}")
        return []
