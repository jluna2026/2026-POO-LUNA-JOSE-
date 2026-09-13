# 🍽️ RESTAURANTE APP - Semana 12
## Programación Orientada a Objetos (POO)

**Autor:** LUNA ÁVILA JOSÉ EDUARDO  
**Curso:** Programación Orientada a Objetos 2026  
**Semana:** 12 - Parcial 2

---

## 📋 Descripción General

**RESTAURANTE APP** es una aplicación de **gestión integral de restaurante** desarrollada en **Python** con enfoque en **Programación Orientada a Objetos (POO)**. 

El sistema permite:
- ✅ Registrar y gestionar usuarios (clientes)
- ✅ Administrar productos (menú del restaurante)
- ✅ Procesar ventas en tiempo real
- ✅ Consultar historial de ventas
- ✅ Controlar el stock de productos
- ✅ Persistir datos en archivos JSON

---

## 📁 Estructura del Proyecto

```
restaurante_app/
│
├── main.py                           # 🎮 Punto de entrada - Menú interactivo
├── README.md                         # 📖 Documentación
│
├── datos/                            # 💾 Almacenamiento de datos (JSON)
│   ├── productos.json               # Base de datos de productos
│   ├── usuarios.json                # Base de datos de usuarios
│   └── ventas.json                  # Registro de transacciones
│
├── modelos/                          # 🏗️ Clases de modelo (POO)
│   ├── __init__.py
│   ├── producto.py                  # Entidad: Producto
│   ├── usuario.py                   # Entidad: Usuario
│   └── venta.py                     # Entidad: Venta
│
└── servicios/                        # ⚙️ Lógica de negocio
    ├── __init__.py
    ├── restaurante.py               # Orquestador principal
    └── archivo_servicio.py          # Servicio de persistencia (JSON)
```

---

## 🏗️ CLASES Y COMPONENTES

### 1. **Clase `Producto`** (`modelos/producto.py`)
Representa un artículo del menú del restaurante.

#### Constructor
```python
def __init__(self, codigo: str, nombre: str, precio: float, stock: int)
```

#### Atributos
| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `codigo` | str | Identificador único (Ej: "001") |
| `nombre` | str | Nombre del producto (Ej: "Arepa de queso") |
| `precio` | float | Precio unitario en pesos |
| `stock` | int | Cantidad disponible en inventario |

#### Métodos
```python
vender(cantidad: int) -> None
```
- Reduce el stock en la cantidad especificada
- Valida que la cantidad sea positiva y no exceda el stock

```python
to_dict() -> dict
```
- Convierte el objeto a diccionario para guardar en JSON

#### Validaciones
- ❌ Stock no puede ser negativo
- ❌ Cantidad a vender debe ser positiva
- ❌ No se puede vender más del stock disponible

#### Ejemplo de uso
```python
producto = Producto("001", "Arepa de queso", 5000.0, 50)
producto.vender(2)      # Reduce stock de 50 a 48
print(producto.stock)   # Output: 48
```

---

### 2. **Clase `Usuario`** (`modelos/usuario.py`)
Representa un cliente del restaurante.

#### Constructor
```python
def __init__(self, identificacion: str, nombre: str)
```

#### Atributos
| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `identificacion` | str | Cédula (exactamente 10 dígitos) |
| `nombre` | str | Nombre completo del cliente |

#### Métodos
```python
to_dict() -> dict
```
- Convierte el objeto a diccionario para guardar en JSON

#### Validaciones
- ❌ Identificación debe ser exactamente 10 dígitos
- ✅ Valida con expresión regular: `r"\d{10}"`

#### Ejemplo de uso
```python
usuario = Usuario("1234567890", "José Luna")           # ✅ Válido
usuario = Usuario("123456789", "María")                # ❌ Error: menos de 10 dígitos
usuario = Usuario("123456789a", "Carlos")              # ❌ Error: contiene letra
```

---

### 3. **Clase `Venta`** (`modelos/venta.py`)
Registra cada transacción de compra realizada.

#### Constructor
```python
def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int, fecha: str = None)
```

#### Atributos
| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `usuario_id` | str | Identificación del cliente que compró |
| `producto_codigo` | str | Código del producto vendido |
| `cantidad` | int | Cantidad de unidades vendidas |
| `fecha` | str | Timestamp (YYYY-MM-DD HH:MM:SS) |

#### Métodos
```python
to_dict() -> dict
```
- Convierte el objeto a diccionario para guardar en JSON

#### Características
- ✅ Fecha se genera automáticamente si no se proporciona
- ✅ Usa `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`

#### Validaciones
- ❌ Cantidad debe ser mayor a cero

#### Ejemplo de uso
```python
venta = Venta("1234567890", "001", 2)
# Output: Venta(usuario_id="1234567890", producto_codigo="001", 
#              cantidad=2, fecha="2026-09-06 22:50:16")
```

---

### 4. **Clase `Restaurante`** (`servicios/restaurante.py`)
Orquestador principal que gestiona toda la lógica de negocio.

#### Constructor
```python
def __init__(self)
```
- Inicializa listas y diccionarios vacíos
- Carga datos desde archivos JSON automáticamente

#### Atributos Privados (Encapsulamiento)
| Atributo | Tipo | Descripción |
|----------|------|-------------|
| `_productos` | list | Lista de objetos Producto |
| `_usuarios` | list | Lista de objetos Usuario |
| `_ventas` | list | Lista de objetos Venta |
| `_productos_dict` | dict | Búsquedas O(1) por código |
| `_usuarios_dict` | dict | Búsquedas O(1) por ID |

#### Métodos Principales

**`cargar_datos()`**
```python
def cargar_datos(self) -> None
```
- Carga datos desde archivos JSON
- Reconstruye diccionarios de búsqueda
- Se ejecuta automáticamente en `__init__`

**`agregar_usuario(usuario: Usuario)`**
```python
def agregar_usuario(self, usuario: Usuario) -> None
```
- Registra un nuevo usuario
- Evita duplicados verificando en diccionario
- Guarda automáticamente en JSON
- Muestra advertencia si usuario ya existe

**`agregar_producto(producto: Producto)`**
```python
def agregar_producto(self, producto: Producto) -> None
```
- Registra un nuevo producto
- Evita duplicados verificando en diccionario
- Guarda automáticamente en JSON
- Muestra advertencia si producto ya existe

**`buscar_usuario(identificacion: str) -> Usuario | None`**
```python
def buscar_usuario(self, identificacion: str) -> Usuario | None
```
- Búsqueda O(1) por identificación
- Retorna el usuario o None si no existe

**`buscar_producto(codigo: str) -> Producto | None`**
```python
def buscar_producto(self, codigo: str) -> Producto | None
```
- Búsqueda O(1) por código
- Retorna el producto o None si no existe

**`vender_producto(codigo_producto, identificacion_usuario, cantidad) -> bool`**
```python
def vender_producto(self, codigo_producto: str, 
                   identificacion_usuario: str, 
                   cantidad: int) -> bool
```

**Proceso:**
1. Busca usuario y producto
2. Valida que existan
3. Valida cantidad > 0
4. Valida stock suficiente
5. Si todo es válido:
   - Crea objeto Venta
   - Reduce stock del producto
   - Guarda cambios en JSON
   - Retorna True
6. Si falla: Retorna False

**`ventas_usuario(identificacion: str) -> list[Venta]`**
```python
def ventas_usuario(self, identificacion: str) -> list[Venta]
```
- Retorna todas las ventas de un usuario
- Filtra por `usuario_id`
- Complejidad O(n)

**`productos_ordenados_por_stock() -> list[Producto]`**
```python
def productos_ordenados_por_stock(self) -> list[Producto]
```
- Retorna productos ordenados por stock
- Orden: mayor → menor cantidad
- Complejidad O(n log n)

**Métodos de Persistencia:**
```python
guardar_productos()    # Persiste lista de productos en JSON
guardar_usuarios()     # Persiste lista de usuarios en JSON
guardar_ventas()       # Persiste lista de ventas en JSON
```

---

### 5. **Clase `ArchivoServicio`** (`servicios/archivo_servicio.py`)
Maneja lectura y escritura de datos en archivos JSON.

#### Métodos Estáticos

**`guardar(nombre_archivo: str, datos: dict | list) -> bool`**
```python
@staticmethod
def guardar(nombre_archivo, datos) -> bool
```

**Características:**
- Escribe datos en formato JSON
- Usa codificación UTF-8
- Indenta el JSON para legibilidad (4 espacios)
- `ensure_ascii=False` para caracteres especiales

**Manejo de excepciones:**
- ✅ `PermissionError`: Sin permisos, muestra mensaje de error
- Retorna True si éxito, False si error

**Ejemplo:**
```python
datos = [{"codigo": "001", "nombre": "Arepa", "precio": 5000}]
ArchivoServicio.guardar("datos/productos.json", datos)
```

**`cargar(nombre_archivo: str) -> list | dict`**
```python
@staticmethod
def cargar(nombre_archivo) -> list | dict
```

**Características:**
- Lee archivo JSON
- Parsea el contenido
- Retorna estructura vacía como fallback

**Manejo de excepciones:**
- ✅ `FileNotFoundError`: Archivo no existe → retorna []
- ✅ `JSONDecodeError`: JSON inválido → muestra error, retorna []

**Ejemplo:**
```python
productos = ArchivoServicio.cargar("datos/productos.json")
# Output: Lista de diccionarios de productos o []
```

---

## 🎮 INTERFAZ DE USUARIO - Menú Principal

### Pantalla Principal
```
===== RESTAURANTE =====
1. Registrar usuario
2. Registrar producto
3. Vender producto
4. Consultar ventas usuario
5. Listar productos por stock
6. Salir

Seleccione una opción:
```

### Flujo Detallado de Cada Opción

#### **OPCIÓN 1: Registrar Usuario**

**Entrada solicitada:**
```
Identificación (10 dígitos): 1234567890
Nombre: José Luna
```

**Proceso:**
1. Crea objeto `Usuario` con validación
2. Si es válido, agrega a la lista y diccionario
3. Guarda en `datos/usuarios.json`

**Posibles salidas:**
- ✅ `"✅ Usuario registrado"` - Éxito
- ⚠️ `"⚠️ Identificación inválida (debe tener 10 dígitos)"` - Formato inválido
- ⚠️ `"⚠️ Usuario ya registrado"` - Duplicado

---

#### **OPCIÓN 2: Registrar Producto**

**Entrada solicitada:**
```
Código: 001
Nombre: Arepa de queso
Precio: 5000
Stock: 50
```

**Proceso:**
1. Crea objeto `Producto` con validación
2. Si es válido, agrega a la lista y diccionario
3. Guarda en `datos/productos.json`

**Posibles salidas:**
- ✅ `"✅ Producto registrado"` - Éxito
- ⚠️ `"⚠️ El stock no puede ser negativo"` - Stock negativo
- ⚠️ `"⚠️ Producto ya registrado"` - Duplicado

---

#### **OPCIÓN 3: Vender Producto**

**Entrada solicitada:**
```
Identificación usuario: 1234567890
Código producto: 001
Cantidad: 2
```

**Validaciones:**
- ¿Existe el usuario?
- ¿Existe el producto?
- ¿Cantidad > 0?
- ¿Stock >= cantidad?

**Proceso (si todas son válidas):**
1. Reduce stock del producto
2. Crea objeto `Venta` con timestamp
3. Agrega venta al historial
4. Guarda cambios:
   - `datos/productos.json` (stock actualizado)
   - `datos/ventas.json` (nueva venta)

**Posibles salidas:**
- ✅ `"✅ Venta realizada"` - Éxito
- ⚠️ `"⚠️ No fue posible realizar la venta"` - Alguna validación falló

---

#### **OPCIÓN 4: Consultar Ventas Usuario**

**Entrada solicitada:**
```
Identificación usuario: 1234567890
```

**Proceso:**
1. Busca todas las ventas del usuario
2. Filtra por `usuario_id`
3. Muestra información detallada

**Salida (ejemplo):**
```
Producto: 001 | Cantidad: 2 | Fecha: 2026-09-06 22:50:16
Producto: 002 | Cantidad: 1 | Fecha: 2026-09-06 22:55:30
```

**Si no hay ventas:**
```
⚠️ No hay ventas registradas para este usuario
```

---

#### **OPCIÓN 5: Listar Productos por Stock**

**Entrada:** Ninguna

**Proceso:**
1. Obtiene lista completa de productos
2. Ordena por stock (mayor → menor)
3. Muestra formato: `CÓDIGO - NOMBRE | Stock: X`

**Salida (ejemplo):**
```
002 - Bandeja Paisa | Stock: 30
001 - Arepa de queso | Stock: 18
003 - Ajiaco | Stock: 5
```

---

#### **OPCIÓN 6: Salir**
```
👋 Programa finalizado
```
Cierra la aplicación.

---

## 💾 FORMATO DE DATOS JSON

### `datos/productos.json`
```json
[
    {
        "codigo": "001",
        "nombre": "Arepa de queso",
        "precio": 5000.0,
        "stock": 50
    },
    {
        "codigo": "002",
        "nombre": "Bandeja Paisa",
        "precio": 15000.0,
        "stock": 30
    },
    {
        "codigo": "003",
        "nombre": "Ajiaco",
        "precio": 8000.0,
        "stock": 5
    }
]
```

### `datos/usuarios.json`
```json
[
    {
        "identificacion": "1234567890",
        "nombre": "José Luna"
    },
    {
        "identificacion": "0987654321",
        "nombre": "María García"
    }
]
```

### `datos/ventas.json`
```json
[
    {
        "usuario_id": "1234567890",
        "producto_codigo": "001",
        "cantidad": 2,
        "fecha": "2026-09-06 22:50:16"
    },
    {
        "usuario_id": "1234567890",
        "producto_codigo": "002",
        "cantidad": 1,
        "fecha": "2026-09-06 22:55:30"
    }
]
```

---

## 🚀 INSTALACIÓN Y EJECUCIÓN

### Requisitos
- ✅ Python 3.8 o superior
- ✅ No requiere librerías externas (solo módulos estándar)

### Pasos para ejecutar

**1. Navegar a la carpeta del proyecto:**
```bash
cd Parcial\ 2/Semana\ 12/restaurante_app
```

**2. Ejecutar el programa:**
```bash
python main.py
```

**En Windows (PowerShell/CMD):**
```bash
cd "Parcial 2\Semana 12\restaurante_app"
python main.py
```

### Primera Ejecución
- Los archivos JSON se crearán automáticamente
- Las carpetas `datos/` debe existir (crear si no está)
- Sistema listo para comenzar a usar

---

## ✅ VALIDACIONES IMPLEMENTADAS

### Validación de Usuario
```python
# Validación: identificación = exactamente 10 dígitos
if not re.fullmatch(r"\d{10}", identificacion):
    raise ValueError("Identificación inválida (debe tener 10 dígitos)")
```
- ❌ "123456789" → Falla (9 dígitos)
- ❌ "12345678a0" → Falla (contiene letra)
- ✅ "1234567890" → Válido

### Validación de Producto
```python
# Validación: stock no puede ser negativo
if stock < 0:
    raise ValueError("El stock no puede ser negativo")

# Validación: cantidad a vender debe ser positiva
if cantidad <= 0:
    raise ValueError("Cantidad inválida")

# Validación: no vender más del disponible
if cantidad > self.stock:
    raise ValueError("Stock insuficiente")
```

### Validación de Venta
```python
# Validación en el orquestador
if usuario is None or producto is None or cantidad <= 0 or producto.stock < cantidad:
    return False
```
- Valida existencia de usuario
- Valida existencia de producto
- Valida cantidad > 0
- Valida stock suficiente

### Validación de Archivos
- ✅ `FileNotFoundError`: Retorna lista vacía
- ✅ `JSONDecodeError`: Muestra error, retorna lista vacía
- ✅ `PermissionError`: Muestra error de permisos

---

## 🔍 CONCEPTOS POO IMPLEMENTADOS

| Concepto | Implementación | Beneficio |
|----------|---|---|
| **Encapsulamiento** | Atributos privados (`_productos`, `_usuarios`) con acceso mediante métodos | Protege integridad de datos |
| **Abstracción** | Modelos representan entidades reales sin exponer detalles internos | Simplifica interfaz de usuario |
| **Clases** | Usuario, Producto, Venta, Restaurante, ArchivoServicio | Organiza código en entidades lógicas |
| **Composición** | Restaurante compone Usuario, Producto y Venta | Reutilización y modularidad |
| **Herencia** | No implementada (no necesaria para este nivel) | - |
| **Polimorfismo** | No implementado (no necesario para este nivel) | - |
| **Métodos Estáticos** | ArchivoServicio usa métodos estáticos | Funcionalidad sin instancia |
| **Excepciones** | `ValueError` en constructores y métodos | Validación robusta |
| **Serialización** | Método `to_dict()` en cada modelo | Convierte objetos a JSON |
| **Búsqueda Eficiente** | Diccionarios para O(1) | Mejor rendimiento |

---

## 📊 COMPLEJIDAD ALGORÍTMICA

| Operación | Complejidad | Razón |
|-----------|---|---|
| Buscar producto por código | O(1) | Acceso directo a diccionario |
| Buscar usuario por ID | O(1) | Acceso directo a diccionario |
| Agregar producto | O(1) | Append + inserción en dict |
| Agregar usuario | O(1) | Append + inserción en dict |
| Realizar venta | O(1) | Búsquedas O(1) + operaciones constantes |
| Ventas de un usuario | O(n) | Itera sobre n ventas |
| Ordenar productos | O(n log n) | Algoritmo sort de Python |
| Cargar datos | O(n) | Lee n registros de JSON |
| Guardar datos | O(n) | Escribe n registros en JSON |

---

## 🐛 MANEJO DE EXCEPCIONES

| Excepción | Origen | Manejo | Línea |
|-----------|--------|--------|-------|
| `ValueError` | Usuario, Producto, Venta | Try-except en main.py | 21-26, 31-38 |
| `FileNotFoundError` | ArchivoServicio.cargar | Retorna [] | 20-21 |
| `JSONDecodeError` | ArchivoServicio.cargar | Muestra error, retorna [] | 22-24 |
| `PermissionError` | ArchivoServicio.guardar | Muestra error de permisos | 11-13 |
| `ValueError` | Producto.vender | Propaga al orquestador | 10-14 |

---

## 🔄 FLUJO DE DATOS GENERAL

```
┌─────────────────────────────────────────┐
│         main.py (Menú Principal)        │
└─────────────────────┬───────────────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
    ┌────────────┐           ┌────────────────┐
    │  Entrada   │           │  Procesamiento │
    │    del     │           │    Lógica      │
    │  Usuario   │           │  (Restaurante) │
    └────────┬───┘           └────────┬───────┘
             │                        │
             │       ┌────────────────┼────────────────┐
             │       ▼                ▼                ▼
             │   ┌────────┐      ┌──────────┐   ┌──────────┐
             │   │Usuario │      │Producto  │   │  Venta   │
             │   └────┬───┘      └────┬─────┘   └────┬─────┘
             │        │              │              │
             └────────┼──────────────┼──────────────┘
                      │              │
                      ▼              ▼
             ┌──────────────────────────────┐
             │   ArchivoServicio (JSON)     │
             └──────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
    ┌────────┐   ┌────────┐   ┌────────┐
    │Productos│   │Usuarios│   │ Ventas │
    │.json    │   │.json   │   │.json   │
    └────────┘   └────────┘   └────────┘
```

---

## 📝 NOTAS DE IMPLEMENTACIÓN

### Seguridad de Datos
- ✅ Atributos privados (`_`) previenen acceso directo
- ✅ Acceso controlado mediante métodos públicos
- ✅ Validaciones en constructores previenen estados inválidos
- ✅ No se permiten duplicados

### Rendimiento
- ✅ Diccionarios para búsquedas O(1)
- ✅ Listas mantenidas para iteración y ordenamiento
- ✅ Sincronización automática entre estructuras

### Persistencia
- ✅ Guardado automático en cada modificación
- ✅ Carga automática al inicializar
- ✅ Recuperación de archivos inexistentes

### Código Limpio
- ✅ Separación clara de responsabilidades
- ✅ Nombres descriptivos
- ✅ Métodos con propósito único
- ✅ Comentarios donde es necesario

---

## 🧪 PRUEBAS REALIZADAS

### ✅ Registro de Usuarios
- [x] Usuario con identificación válida (10 dígitos)
- [x] Usuario con identificación inválida (menos de 10 dígitos)
- [x] Usuario con identificación inválida (contiene letras)
- [x] Prevención de usuarios duplicados
- [x] Datos persisten en JSON

### ✅ Registro de Productos
- [x] Producto con datos válidos
- [x] Producto con stock negativo (rechazado)
- [x] Prevención de productos duplicados
- [x] Datos persisten en JSON

### ✅ Ventas
- [x] Venta con stock suficiente (éxito)
- [x] Venta con stock insuficiente (falla)
- [x] Venta con usuario inexistente (falla)
- [x] Venta con producto inexistente (falla)
- [x] Stock se reduce correctamente
- [x] Venta se registra con timestamp

### ✅ Consultas
- [x] Búsqueda de ventas por usuario (encuentra todas)
- [x] Búsqueda de usuario inexistente (retorna vacío)
- [x] Ordenamiento de productos por stock (de mayor a menor)

### ✅ Persistencia
- [x] Datos persisten después de reiniciar
- [x] Archivos JSON se crean si no existen
- [x] Datos se recuperan correctamente
- [x] Cambios se reflejan en JSON

---

## 📚 RESUMEN TÉCNICO

**Paradigma:** Programación Orientada a Objetos  
**Lenguaje:** Python 3.8+  
**Módulos utilizados:** `json`, `datetime`, `re`  
**Patrones:** MVC simplificado (Modelo-Vista-Control)  
**Persistencia:** JSON (sin base de datos)  
**Validación:** Excepciones (POO)  
**Búsqueda:** Diccionarios (O(1))  

---

## 🎓 Conclusión

RESTAURANTE APP demuestra la implementación correcta de conceptos fundamentales de **Programación Orientada a Objetos**:

1. **Encapsulamiento:** Protección de datos internos
2. **Validación:** Uso de excepciones para asegurar integridad
3. **Composición:** Integración de clases relacionadas
4. **Persistencia:** Almacenamiento y recuperación de datos
5. **Interfaz de usuario:** Menú interactivo y amigable
6. **Código limpio:** Separación de responsabilidades

El sistema es robusto, escalable y fácil de mantener.

---

## 📞 Contacto y Soporte

**Autor:** LUNA ÁVILA JOSÉ EDUARDO  
**Institución:** Programación Orientada a Objetos 2026  
**Semana:** 12  

---

**© 2026 - Todos los derechos reservados**
