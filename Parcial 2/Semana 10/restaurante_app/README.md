# Restaurante App

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO) para gestionar productos de un restaurante.

La aplicación permite registrar, consultar, actualizar y eliminar productos, además de almacenar la información en un archivo JSON para mantener los datos disponibles entre ejecuciones del programa.

---

## Estructura del Proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

---

## Funcionalidades

La aplicación permite:

- Agregar productos.
- Listar productos registrados.
- Buscar productos por código.
- Actualizar información de productos.
- Eliminar productos.
- Guardar información en archivos JSON.
- Recuperar información almacenada al iniciar la aplicación.

---

## Clases Implementadas

### Producto

Representa un producto del restaurante.

**Atributos:**

- codigo
- nombre
- precio

**Métodos principales:**

- `a_diccionario()`
- `desde_diccionario()`

---

### Usuario

Representa un usuario del sistema.

**Atributos:**

- id_usuario
- nombre
- correo

---

### Restaurante

Gestiona los productos registrados en memoria.

**Responsabilidades:**

- Agregar productos.
- Buscar productos.
- Listar productos.
- Actualizar productos.
- Eliminar productos.

---

### ArchivoServicio

Gestiona la persistencia de datos.

**Responsabilidades:**

- Leer el archivo JSON.
- Guardar información en el archivo JSON.
- Convertir objetos Producto en diccionarios.
- Convertir diccionarios en objetos Producto.
- Manejar excepciones relacionadas con archivos.

---

## Persistencia de Datos

La información se almacena en el siguiente archivo:

```text
datos/productos.json
```

### Ejemplo de contenido

```json
[
    {
        "codigo": "00",
        "nombre": "HAMBURGUESA",
        "precio": 3.0
    },
    {
        "codigo": "01",
        "nombre": "SALCHIPAPA",
        "precio": 3.0
    }
]
```

---

## Manejo de Excepciones

La aplicación implementa el manejo de las siguientes excepciones:

- FileNotFoundError
- JSONDecodeError
- ValueError
- PermissionError
- KeyError

---

## Requisitos

- Python 3.10 o superior
- PyCharm o cualquier IDE compatible con Python

---

## Ejecución

Desde la carpeta principal del proyecto ejecutar:

```bash
python main.py
```

---

## Menú Principal

```text
===== RESTAURANTE =====

1. Agregar producto
2. Listar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Salir
```

---

## Prueba de Persistencia

1. Ejecutar la aplicación.
2. Agregar un producto.
3. Verificar que el archivo `productos.json` se actualice.
4. Cerrar el programa.
5. Ejecutar nuevamente la aplicación.
6. Listar productos.
7. Confirmar que la información permanece almacenada.

---

## Tecnologías Utilizadas

- Python
- Programación Orientada a Objetos (POO)
- Archivos JSON
- Manejo de archivos
- Manejo de excepciones

---

## Autor

**José Eduardo Luna Ávila**

Proyecto académico desarrollado para la materia de Programación Orientada a Objetos.