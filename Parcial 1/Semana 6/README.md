# 🍽️ Sistema de Gestión de Restaurante - Semana 6

## 📝 Descripción General

Este proyecto implementa un **sistema de gestión de restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite crear y gestionar platillos y bebidas en un restaurante, demostrando conceptos clave como **herencia**, **encapsulación** y **polimorfismo**.

---

## 📂 Estructura del Proyecto

```
restaurante_app/
├── main.py                 # Punto de entrada de la aplicación
├── modelos/               # Módulo con las clases de datos
│   ├── __init__.py
│   ├── producto.py        # Clase base para productos
│   ├── platillo.py        # Clase para platillos
│   └── bebida.py          # Clase para bebidas
└── servicios/             # Módulo con lógica de negocio
    ├── __init__.py
    └── restaurante.py     # Clase para gestionar el restaurante
```

---

## 🔍 Explicación Detallada del Código

### 1️⃣ **Clase `Producto` (modelos/producto.py)**

**Propósito:** Clase base que define la estructura común para todos los productos del restaurante.

```python
class Producto:
    def __init__(self, nombre, precio, disponible=True):
        self._nombre = nombre
        self._precio = precio
        self._disponible = disponible
```

**Componentes:**

| Método | Descripción |
|--------|-------------|
| `__init__()` | Constructor que inicializa los atributos básicos del producto |
| `obtener_precio()` | Retorna el precio actual del producto |
| `cambiar_precio(nuevo_precio)` | Permite modificar el precio (con validación) |
| `mostrar_informacion()` | Retorna una representación en texto del producto |

**Características:**
- Usa **encapsulación** con atributos privados (`_nombre`, `_precio`, `_disponible`)
- Valida que el precio sea mayor a cero antes de actualizarlo
- Método `mostrar_informacion()` será sobrescrito en las subclases (polimorfismo)

---

### 2️⃣ **Clase `Platillo` (modelos/platillo.py)**

**Propósito:** Subclase que especializa `Producto` para representar platillos con información nutricional.

```python
class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias
```

**Conceptos POO Utilizados:**

| Concepto | Implementación |
|----------|----------------|
| **Herencia** | Extiende la clase `Producto` |
| **Polimorfismo** | Sobrescribe `mostrar_informacion()` |
| **super()** | Llama al constructor de la clase padre |

**Método específico:**
- `mostrar_informacion()`: Retorna información del platillo con emoji 🍽️, incluyendo calorías

**Ejemplo de salida:**
```
🍽️ Platillo: Arroz con pollo | Precio: $3.50 | Calorías: 600
```

---

### 3️⃣ **Clase `Bebida` (modelos/bebida.py)**

**Propósito:** Subclase que especializa `Producto` para representar bebidas con información de volumen.

```python
class Bebida(Producto):
    def __init__(self, nombre, precio, mililitros, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.mililitros = mililitros
```

**Características:**
- Similar a `Platillo`, pero agrega el atributo `mililitros` en lugar de calorías
- Sobrescribe `mostrar_informacion()` con presentación específica para bebidas

**Método específico:**
- `mostrar_informacion()`: Retorna información de la bebida con emoji 🥤

**Ejemplo de salida:**
```
🥤 Bebida: Jugo de naranja | Precio: $1.50 | Tamaño: 300 ml
```

---

### 4️⃣ **Clase `Restaurante` (servicios/restaurante.py)**

**Propósito:** Clase que gestiona el restaurante y su menú de productos.

```python
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
```

**Métodos:**

| Método | Descripción |
|--------|-------------|
| `__init__(nombre)` | Crea un restaurante con un nombre e inicializa lista vacía de productos |
| `agregar_producto(producto)` | Añade un producto (Platillo o Bebida) al menú |
| `mostrar_menu()` | Imprime el menú completo del restaurante |

**Responsabilidades:**
- Mantener una colección de productos
- Gestionar la adición de productos
- Mostrar el menú de forma formateada

---

### 5️⃣ **Archivo Principal (main.py)**

**Propósito:** Demuestra cómo usar el sistema.

**Flujo de ejecución:**

```python
def main():
    # 1️⃣ Crear instancia del restaurante
    restaurante = Restaurante("La Tía Lea")

    # 2️⃣ Crear productos
    platillo1 = Platillo("Arroz con pollo", 3.50, 600)
    platillo2 = Platillo("Ceviche", 4.00, 450)
    bebida1 = Bebida("Jugo de naranja", 1.50, 300)
    bebida2 = Bebida("Coca-Cola", 1.20, 350)

    # 3️⃣ Agregar al restaurante
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    # 4️⃣ Mostrar menú
    restaurante.mostrar_menu()
```

**Salida esperada:**
```
📋 Menú del restaurante La Tía Lea:
🍽️ Platillo: Arroz con pollo | Precio: $3.50 | Calorías: 600
🍽️ Platillo: Ceviche | Precio: $4.00 | Calorías: 450
🥤 Bebida: Jugo de naranja | Precio: $1.50 | Tamaño: 300 ml
🥤 Bebida: Coca-Cola | Precio: $1.20 | Tamaño: 350 ml
```

---

## 🎓 Conceptos POO Aplicados

### 1. **Encapsulación**
- Atributos privados en `Producto` (con prefijo `_`)
- Acceso controlado mediante métodos como `obtener_precio()` y `cambiar_precio()`

### 2. **Herencia**
- `Platillo` y `Bebida` heredan de `Producto`
- Comparten comportamiento común y agregan funcionalidad específica

### 3. **Polimorfismo**
- Ambas subclases sobrescriben `mostrar_informacion()`
- Cada una tiene su propia implementación personalizada
- Se puede llamar el mismo método en diferentes tipos de productos

### 4. **Abstracción**
- Los detalles internos están ocultos
- La interfaz es simple: crear productos y agregarlos al restaurante

---

## 🚀 Cómo Ejecutar

1. Asegúrate de estar en el directorio del proyecto
2. Ejecuta el archivo principal:

```bash
python main.py
```

---

## 💡 Posibles Extensiones

- ✅ Agregar método para eliminar productos
- ✅ Calcular el precio total del menú
- ✅ Filtrar productos por rango de precio
- ✅ Agregar categorías de productos
- ✅ Implementar un sistema de pedidos
- ✅ Guardar/cargar menú desde archivo

---

## 📌 Notas Importantes

- El proyecto demuestra **buenas prácticas** de POO
- La **modularidad** permite que sea fácil de mantener y extender
- El uso de **emojis** hace la salida más visual e intuitiva
- La **validación de datos** asegura integridad (ej: precio > 0)

---

**Autor:** Jose Luna Ávila  
**Materia:** Programación Orientada a Objetos (POO)  
**Semana:** 6 - 2026
