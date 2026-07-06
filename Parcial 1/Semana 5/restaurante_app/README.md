# 📚 Guía de Programación Orientada a Objetos (POO) - Sistema de Restaurante

**Nivel:** Principiante en POO  
**Autor:** Jose Luna Ávila  
**Semana:** 5 - 2026

---

## 🎯 Introducción: ¿Qué es la Programación Orientada a Objetos?

Imagina que quieres crear un programa para un restaurante. Podrías escribir todo en una sola función gigante, pero eso sería desordenado y difícil de mantener.

**La Programación Orientada a Objetos (POO)** nos permite organizar el código de forma más natural, usando **objetos** que representan cosas del mundo real:

```
Mundo Real          →  Código POO
├─ Restaurante      →  Clase Restaurante
├─ Cliente          →  Clase Cliente
└─ Producto         →  Clase Producto
```

---

## 🧩 Concepto 1: Clases y Objetos

### ¿Qué es una Clase?

Una **clase** es como un **plano o molde** para crear objetos. Es la definición de qué características y comportamientos tendrá algo.

```
CLASE = PLANO/MOLDE
OBJETO = COSA CREADA A PARTIR DEL PLANO
```

**Analogía del mundo real:**
```
Clase Galleta    = Receta de galletas (el plano)
Objeto Galleta   = Una galleta que hiciste siguiendo la receta
```

### Ejemplo en este proyecto: Clase Cliente

```python
class Cliente:
    def __init__(self, nombre: str, edad: int, es_vip: bool):
        self.nombre = nombre
        self.edad = edad
        self.es_vip = es_vip
```

**En `main.py` creamos objetos Cliente:**
```python
c1 = Cliente("Ana Pérez", 25, True)    # Objeto 1
c2 = Cliente("Luis Gómez", 32, False)  # Objeto 2
```

Ambos son clientes, pero tienen información diferente. Es como tener dos moldes para galletas pero hacer galletas de diferente tamaño.

---

## 🏗️ Concepto 2: Atributos (Características)

Los **atributos** son las características o propiedades de un objeto.

### Ejemplo: Clase Producto

```python
class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre          # ← Atributo 1
        self.precio = precio          # ← Atributo 2
        self.disponible = disponible  # ← Atributo 3
```

**¿Qué significa cada línea?**

| Línea | Explicación |
|-------|-------------|
| `self.nombre = nombre` | Guarda el nombre del producto en la memoria |
| `self.precio = precio` | Guarda el precio del producto |
| `self.disponible = disponible` | Guarda si está disponible (True/False) |

**¿Qué es `self`?**
- `self` significa **"yo mismo"** o **"este objeto"**
- Le dice al objeto: "guarda tu nombre aquí", "guarda tu precio aquí"
- Es como si cada objeto llevara una etiqueta con su información

**Creando un objeto con atributos:**
```python
p1 = Producto("Hamburguesa clásica", 5.50, True)
```

Ahora `p1` tiene:
- `p1.nombre = "Hamburguesa clásica"`
- `p1.precio = 5.50`
- `p1.disponible = True`

---

## ⚙️ Concepto 3: Métodos (Acciones)

Los **métodos** son las acciones o comportamientos que puede hacer un objeto.

### Ejemplo: Métodos en la Clase Producto

```python
def aplicar_descuento(self, porcentaje: float) -> None:
    """Aplica un descuento al precio del producto."""
    if porcentaje > 0:
        self.precio = self.precio * (1 - porcentaje / 100)
```

**¿Qué hace este método?**
1. Recibe un porcentaje como parámetro
2. Multiplica el precio por (1 - porcentaje/100)
3. Actualiza el precio del producto

**Ejemplo de uso:**
```python
p1 = Producto("Pizza margarita", 7.25, True)
print(p1.precio)           # Salida: 7.25
p1.aplicar_descuento(10)   # Aplica 10% de descuento
print(p1.precio)           # Salida: 6.525
```

### Otro método: `__str__`

```python
def __str__(self) -> str:
    estado = "Disponible" if self.disponible else "No disponible"
    return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado}"
```

**¿Por qué `__str__`?**
- Los dos guiones bajos (`__`) indican que es un método especial
- `__str__` se ejecuta cuando imprimimos el objeto con `print()`

**Ejemplo:**
```python
p1 = Producto("Hamburguesa clásica", 5.50, True)
print(p1)  # Salida: Producto: Hamburguesa clásica | Precio: $5.50 | Estado: Disponible
```

---

## 🏢 Concepto 4: La Clase Restaurante (Contenedor)

La clase `Restaurante` es especial porque **contiene a otras clases** (Productos y Clientes).

```python
class Restaurante:
    def __init__(self, nombre: str, abierto: bool):
        self.nombre = nombre              # str
        self.abierto = abierto            # bool
        self.productos = []               # Lista vacía
        self.clientes = []                # Lista vacía
```

**Puntos importantes:**
- `self.productos = []` crea una lista vacía que guardará objetos Producto
- `self.clientes = []` crea una lista vacía que guardará objetos Cliente

### Métodos para registrar cosas

```python
def registrar_producto(self, producto: Producto) -> None:
    """Registra un producto en la lista de productos."""
    if producto not in self.productos:
        self.productos.append(producto)
```

**Explicación:**
1. Verifica si el producto ya está en la lista (`if producto not in self.productos`)
2. Si no está, lo añade con `append()`

**Analogía:** Es como tener una lista en una hoja de papel. Antes de escribir algo, verificas que no esté ya escrito.

### Métodos para listar información

```python
def listar_productos(self) -> str:
    """Devuelve un texto con todos los productos registrados."""
    if not self.productos:
        return "No hay productos registrados."
    return "\n".join(str(p) for p in self.productos)
```

**Explicación paso a paso:**
1. `if not self.productos:` → Si la lista está vacía
2. Retorna un mensaje indicando que no hay productos
3. Si hay productos, `"\n".join(...)` combina todos los productos en un texto

---

## 📂 Estructura del Proyecto

### Organización de carpetas

```
restaurante_app/
├── main.py                    # Punto de entrada
├── modelos/                   # Clases que representan cosas
│   ├── __init__.py
│   ├── cliente.py             # Clase Cliente
│   └── producto.py            # Clase Producto
└── servicios/                 # Clases que coordinan
    ├── __init__.py
    └── restaurante.py         # Clase Restaurante
```

**¿Por qué esta estructura?**
- **modelos/** → Aquí van las clases que representan datos
- **servicios/** → Aquí van las clases que usan esos datos y organizan lógica

---

## 🔄 Flujo del Programa Principal (main.py)

### Paso 1: Importar las clases

```python
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
```

Traemos las clases desde donde están guardadas. Es como traer herramientas de diferentes cajones.

### Paso 2: Crear funciones auxiliares

```python
def crear_productos_generales():
    """Crea productos generales del restaurante."""
    p1 = Producto("Hamburguesa clásica", 5.50, True)
    p2 = Producto("Pizza margarita", 7.25, True)
    return [p1, p2]
```

Esta función crea objetos Producto y los devuelve en una lista.

```python
def crear_clientes():
    """Crea clientes registrados."""
    c1 = Cliente("Ana Pérez", 25, True)
    c2 = Cliente("Luis Gómez", 32, False)
    return [c1, c2]
```

Esta función crea objetos Cliente y los devuelve en una lista.

### Paso 3: Función main - Orquestar todo

```python
def main():
    # 1. Crear el restaurante
    restaurante = Restaurante("La Buena Mesa", abierto=True)

    # 2. Registrar productos
    for producto in crear_productos_generales():
        restaurante.registrar_producto(producto)

    # 3. Registrar clientes
    for cliente in crear_clientes():
        restaurante.registrar_cliente(cliente)

    # 4. Mostrar toda la información
    print(restaurante)
```

**¿Qué sucede aquí?**
1. Se crea un objeto Restaurante
2. Se crea una lista de productos y se añaden al restaurante
3. Se crea una lista de clientes y se añaden al restaurante
4. Se imprime toda la información del restaurante

---

## 📊 Diagrama de Relaciones

```
┌─────────────────────────────────────┐
│         RESTAURANTE                 │
│  (Contenedor principal)             │
├─────────────────────────────────────┤
│ Atributos:                          │
│ • nombre                            │
│ • abierto                           │
│ • productos [Lista]  ────────────┐  │
│ • clientes [Lista]   ────────────┼──┼─> Métodos para
│                                  │  │   organizar todo
│ Métodos:                         │  │
│ • registrar_producto()           │  │
│ • registrar_cliente()            │  │
│ • listar_productos()             │  │
│ • listar_clientes()              │  │
└─────────────────────────────────────┘
         ▲                    ▲
         │                    │
         │                    │
┌────────────────┐   ┌────────────────┐
│   PRODUCTO     │   │    CLIENTE     │
├────────────────┤   ├────────────────┤
│ Atributos:     │   │ Atributos:     │
│ • nombre       │   │ • nombre       │
│ • precio       │   │ • edad         │
│ • disponible   │   │ • es_vip       │
│                │   │                │
│ Métodos:       │   │ Métodos:       │
│ • descuento()  │   │ • activar_vip()│
│ • no_disponible│   │ • desactivar..│
│ • __str__()    │   │ • __str__()    │
└────────────────┘   └────────────────┘
```

---

## 🎓 Los 4 Pilares de la POO

### 1. **Encapsulación** (Proteger datos)

En este proyecto los datos están dentro de las clases. Un producto no puede existir fuera de un `Producto`.

```python
# Correcto ✅
p1 = Producto("Pizza", 7.25, True)

# Incorrecto ❌
precio = 7.25  # Precio sin contexto
```

### 2. **Abstracción** (Simplificar complejidad)

El usuario solo usa `restaurante.registrar_producto()` sin saber todos los detalles internos.

```python
# Simple para el usuario
restaurante.registrar_producto(p1)

# Pero internamente hace:
# - Verifica si ya existe
# - Lo añade a la lista
# - Etc.
```

### 3. **Herencia** (Compartir código)

⚠️ Este proyecto no la usa, pero la verás en Semana 6.

### 4. **Polimorfismo** (Muchas formas)

⚠️ Este proyecto no la usa mucho, pero en Semana 6 lo verás.

---

## 💻 Cómo Ejecutar el Programa

### Opción 1: Desde terminal

```bash
cd C:\Users\c-jluna\PycharmProjects\2026-POO-LUNA-JOSE-\Parcial 1\Semana 5
python -m restaurante_app.main
```

### Opción 2: Desde PyCharm

1. Haz clic derecho en `main.py`
2. Selecciona "Run 'main'"

### Salida esperada:

```
Restaurante: La Buena Mesa | Estado: Abierto
--- Productos ---
Producto: Hamburguesa clásica | Precio: $5.50 | Estado: Disponible
Producto: Pizza margarita | Precio: $7.25 | Estado: Disponible
--- Clientes ---
Cliente: Ana Pérez | Edad: 25 | Tipo: VIP
Cliente: Luis Gómez | Edad: 32 | Tipo: Regular
```

---

## 🧪 Ejemplo Interactivo: Vamos paso a paso

Imagina que quieres usar este código en Python:

### Paso 1: Crear un producto
```python
from modelos.producto import Producto

hamburgesa = Producto("Hamburguesa", 5.50, True)
```
Ahora `hamburgesa` es un objeto que tiene:
- nombre = "Hamburguesa"
- precio = 5.50
- disponible = True

### Paso 2: Usar métodos
```python
print(hamburgesa)  # Mostramos el producto
# Salida: Producto: Hamburguesa | Precio: $5.50 | Estado: Disponible

hamburgesa.aplicar_descuento(20)  # Aplicamos 20% descuento
print(hamburgesa.precio)  # Verificamos el precio
# Salida: 4.4
```

### Paso 3: Crear un cliente
```python
from modelos.cliente import Cliente

cliente1 = Cliente("Juan", 30, False)
print(cliente1)  # Mostramos el cliente
# Salida: Cliente: Juan | Edad: 30 | Tipo: Regular

cliente1.activar_vip()  # Lo hacemos VIP
print(cliente1)  # Mostramos nuevamente
# Salida: Cliente: Juan | Edad: 30 | Tipo: VIP
```

### Paso 4: Crear restaurante y agregar todo
```python
from servicios.restaurante import Restaurante

rest = Restaurante("Mi Restaurante", True)
rest.registrar_producto(hamburgesa)
rest.registrar_cliente(cliente1)

print(rest)  # Muestra toda la información
```

---

## ❓ Preguntas Frecuentes para Principiantes

### P: ¿Cuál es la diferencia entre clase y objeto?
**R:** 
- **Clase** = La idea/definición (Plano de una casa)
- **Objeto** = Lo concreto (Una casa construida)

### P: ¿Qué es `self`?
**R:** Es una referencia al objeto mismo. Le dice "este atributo pertenece a este objeto específico".

### P: ¿Por qué separar en carpetas modelos/ y servicios/?
**R:** Para organizar el código:
- **modelos/** = Datos y características
- **servicios/** = Lógica de negocio

### P: ¿Puedo tener múltiples objetos de la misma clase?
**R:** ¡Sí! Puedes crear tantos objetos como quieras. Cada uno es independiente.

### P: ¿Qué es `__init__`?
**R:** Es el "constructor". Se ejecuta automáticamente cuando creas un objeto.

---

## 🚀 Próximos Pasos (Semana 6)

En la semana 6 aprenderás:
- ✅ **Herencia**: Crear clases que heredan de otras clases
- ✅ **Especialización**: Platillo y Bebida heredarán de Producto
- ✅ **Polimorfismo**: El mismo método se comporta diferente según el objeto

---

## 📚 Resumen de Conceptos Clave

| Concepto | Definición | Ejemplo |
|----------|-----------|---------|
| **Clase** | Molde/Plano | `class Producto:` |
| **Objeto** | Instancia de una clase | `p1 = Producto(...)` |
| **Atributo** | Característica | `self.nombre` |
| **Método** | Acción/Comportamiento | `def aplicar_descuento()` |
| **self** | Referencia al objeto | Dentro de métodos |
| **__init__** | Constructor | Inicializa atributos |
| **__str__** | Representación en texto | Para `print()` |

---

## 📝 Conclusión

Este proyecto es un excelente ejemplo de cómo la POO nos ayuda a:
- ✅ Organizar el código de forma clara
- ✅ Reutilizar código (clases como plantillas)
- ✅ Mantener el código fácil de entender
- ✅ Facilitar la expansión del proyecto

¡Felicidades por aprender POO! 🎉

---

**Última actualización:** 5 de Julio de 2026

