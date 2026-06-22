# Sistema de Gestión de Restaurante

UNIVERSIDAD ESTATAL AMAZONICA

**Nombre completo del estudiante:** José Eduardo Luna Ávila

Asignatura: Programación Orientada a Objetos — Semana 4

---

## Descripción del sistema

Este proyecto es un sistema básico de gestión de restaurante desarrollado en
Python mediante Programación Orientada a Objetos (POO). El sistema permite
registrar productos (platos, bebidas, postres) y clientes, y administrarlos a
través de un servicio central que muestra la información de forma organizada en
la consola.

El objetivo principal no es construir una aplicación compleja, sino demostrar la
organización modular del proyecto, la separación de responsabilidades entre
clases y la comunicación entre archivos mediante importaciones.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── producto.py      # Clase Producto (modelo de un producto)
│   └── cliente.py       # Clase Cliente (modelo de un cliente)
├── servicios/
│   └── restaurante.py   # Clase Restaurante (gestiona productos y clientes)
└── main.py              # Punto de arranque del programa
```

### Responsabilidad de cada archivo

- `modelos/producto.py`: define la clase `Producto`, que representa un plato,
  bebida o producto del restaurante (código, nombre, categoría, precio y
  disponibilidad).
- `modelos/cliente.py`: define la clase `Cliente`, que representa a una persona
  que realiza pedidos (cédula, nombre, teléfono y correo).
- `servicios/restaurante.py`: define la clase `Restaurante`, que actúa como
  servicio principal y gestiona las listas de productos y clientes.
- `main.py`: es el punto de arranque. Crea los objetos, los registra en el
  servicio y muestra el funcionamiento del sistema.

> Las carpetas incluyen un archivo `__init__.py` vacío para que Python reconozca
> los módulos y las importaciones funcionen correctamente.

---

## Conceptos de POO aplicados

- Clases y objetos: `Producto`, `Cliente` y `Restaurante`.
- Constructor `__init__()`: inicializa los atributos de cada objeto.
- Atributos: definidos según el contexto del restaurante.
- Métodos: para gestionar y mostrar la información de los objetos.
- Método especial `__str__()`: representa los objetos como texto legible.
- Importaciones entre módulos: comunican los archivos del proyecto.

---

## Cómo ejecutar el programa

1. Ubícate en la carpeta raíz del proyecto (`restaurante_app/`).
2. Ejecuta el archivo principal:

```bash
python main.py
```

El programa mostrará en consola el menú de productos, la lista de clientes
registrados, el total del menú disponible y un ejemplo de búsqueda de producto.

---

## Reflexión sobre modularidad y separación de responsabilidades

Modularizar el software consiste en dividir un programa en partes más pequeñas y
organizadas, donde cada archivo cumple una función clara. Separar las
responsabilidades —los modelos representan los datos, el servicio coordina las
operaciones y `main.py` ejecuta el programa— hace que el código sea más legible,
ordenado y fácil de mantener.

Gracias a esta organización, si en el futuro se necesita modificar o ampliar una
parte del sistema (por ejemplo, agregar un nuevo atributo a `Producto`), solo se
edita el archivo correspondiente sin afectar al resto del proyecto. Esto reduce
errores, facilita el trabajo en equipo y permite reutilizar el código, que son
ventajas fundamentales de la Programación Orientada a Objetos.
