# 🍽️ RESTAURANTE APP - Parcial 2, Semana 14

## 📋 Descripción General

**Restaurante App** es una aplicación de escritorio desarrollada en **Python** con **Tkinter** que permite gestionar la información de un restaurante. La aplicación implementa una arquitectura MVC (Modelo-Vista-Controlador) con servicios especializados, proporcionando funcionalidades de autenticación de usuarios y gestión completa de productos (inventario).

---

## 🎯 Objetivos de la Aplicación

- ✅ Autenticar usuarios del sistema mediante credenciales
- ✅ Listar usuarios registrados en el sistema
- ✅ Registrar nuevos productos en el catálogo
- ✅ Consultar información de productos existentes
- ✅ Actualizar datos de productos (nombre, precio, stock)
- ✅ Eliminar productos del catálogo
- ✅ Persistencia de datos en archivos JSON
- ✅ Validación de datos en modelos y servicios

---

## 📁 Estructura del Proyecto

```
restaurante_app/
├── main.py                          # Punto de entrada de la aplicación
├── datos/                           # Almacenamiento de datos persistentes
│   ├── usuarios.json               # Archivo con usuarios del sistema
│   └── productos.json              # Archivo con productos del catálogo
├── modelos/                         # Clases de dominio (Entidades)
│   ├── __init__.py
│   ├── usuario.py                  # Clase Usuario
│   └── producto.py                 # Clase Producto
├── servicios/                       # Lógica de negocio y persistencia
│   ├── __init__.py
│   ├── archivo_servicio.py         # Servicio para cargar/guardar JSON
│   └── restaurante_servicio.py     # Servicio principal de la aplicación
└── ui/                             # Interfaz gráfica (Vistas)
    ├── __init__.py
    ├── login_view.py               # Pantalla de login
    └── main_view.py                # Pantalla principal con pestañas
```

---

## 🔧 Componentes Principales

### 1️⃣ **Modelos (modelos/)**

#### `usuario.py` - Clase Usuario
Representa un usuario del sistema con validaciones básicas.

**Atributos:**
- `identificacion` (str): ID numérico único del usuario
- `nombre` (str): Nombre del usuario
- `password` (str): Contraseña del usuario

**Métodos:**
- `to_dict()`: Convierte el objeto a diccionario para guardar en JSON
- `__str__()`: Representación en texto del usuario

**Validaciones:**
- La identificación debe ser numérica
- El nombre no puede estar vacío
- La contraseña no puede estar vacía

---

#### `producto.py` - Clase Producto
Representa un producto del catálogo del restaurante.

**Atributos:**
- `codigo` (str): Código único del producto
- `nombre` (str): Nombre del producto
- `precio` (float): Precio unitario del producto
- `stock` (int): Cantidad disponible en inventario

**Métodos:**
- `vender(cantidad)`: Reduce el stock al vender cierta cantidad
- `to_dict()`: Convierte el objeto a diccionario para guardar en JSON
- `__str__()`: Representación en texto del producto

**Validaciones:**
- El código no puede estar vacío
- El precio debe ser mayor a 0
- El stock no puede ser negativo
- No se puede vender más cantidad que la disponible

---

### 2️⃣ **Servicios (servicios/)**

#### `archivo_servicio.py` - ArchivoServicio
Servicio estático para operaciones de lectura y escritura en JSON.

**Métodos estáticos:**
- `guardar(nombre_archivo, datos)`: Guarda datos en archivo JSON con codificación UTF-8
- `cargar(nombre_archivo)`: Carga datos desde archivo JSON

**Características:**
- Manejo de excepciones (FileNotFoundError, PermissionError, JSONDecodeError)
- Retorna lista vacía si el archivo no existe o hay error de formato

---

#### `restaurante_servicio.py` - RestauranteServicio
Servicio principal que orquesta la lógica de negocio de la aplicación.

**Constructores:**
```python
RestauranteServicio(productos=None, usuarios=None)
```

**Métodos de Usuarios:**
- `listar_usuarios()`: Retorna lista de objetos Usuario del sistema
- `validar_usuario(identificacion, password)`: Verifica credenciales de usuario para login

**Métodos de Productos:**
- `listar_productos()`: Retorna todos los productos registrados
- `registrar_producto(codigo, nombre, precio, stock)`: Agrega nuevo producto al catálogo
- `consultar_producto(codigo)`: Busca y retorna un producto por código
- `actualizar_producto(codigo, nombre, precio, stock)`: Modifica datos existentes de un producto
- `eliminar_producto(codigo)`: Remueve un producto del catálogo

**Persistencia:**
- Guarda automáticamente cambios en archivos JSON
- Rutas: `restaurante_app/datos/productos.json` y `restaurante_app/datos/usuarios.json`

---

### 3️⃣ **Interfaz Gráfica (ui/)**

#### `login_view.py` - LoginView
Pantalla de autenticación de usuarios.

**Componentes:**
- Entrada de identificación (texto)
- Entrada de contraseña (oculta con asteriscos)
- Botón "Ingresar"

**Flujo:**
1. El usuario ingresa sus credenciales
2. Se valida contra la base de datos de usuarios
3. Si es válido, se ejecuta el callback hacia la pantalla principal
4. Si es inválido, muestra mensaje de error

---

#### `main_view.py` - MainView
Pantalla principal con la gestión completa del restaurante.

**Estructura:**
- **Interfaz con pestañas (Notebook):**
  - Pestaña "Usuarios": Visualización de usuarios registrados en tabla
  - Pestaña "Productos": Gestión completa de productos

**Pestaña Usuarios:**
- Tabla (Treeview) con dos columnas: Identificación y Nombre
- Visualización de solo lectura de todos los usuarios del sistema

**Pestaña Productos:**
- **Formulario de entrada:** Campos para código, nombre, precio y stock
- **Botones de acción:**
  - Registrar: Agrega nuevo producto
  - Consultar: Busca un producto por código
  - Actualizar: Modifica datos de un producto existente
  - Eliminar: Remueve un producto del catálogo
- **Tabla de productos:** Visualización en tiempo real del inventario

**Botón Global:**
- "Cerrar sesión": Regresa a la pantalla de login

---

### 4️⃣ **Aplicación Principal (main.py)**

Punto de entrada de la aplicación que orquesta todo el flujo.

**Clase `Aplicacion`:**
- **`__init__(root)`**: Inicializa la ventana principal (800x600px)
- **`limpiar_ventana()`**: Limpia todos los widgets de la ventana para cambiar de vista
- **`mostrar_login()`**: Muestra la pantalla de login
- **`mostrar_principal()`**: Muestra la pantalla principal con pestañas

**Flujo de ejecución:**
```
1. Se crea la ventana Tkinter
2. Se carga datos de usuarios.json y productos.json
3. Se instancia RestauranteServicio con los datos cargados
4. Se muestra LoginView
   ├── Usuario ingresa credenciales
   ├── Se valida contra el servicio
   ├── Si es válido → mostrar_principal()
   └── Si es inválido → messagebox.showerror()
5. En MainView el usuario puede:
   ├── Ver tabla de usuarios (pestaña Usuarios)
   ├── Gestionar productos (pestaña Productos)
   └── Cerrar sesión → volver a LoginView
```

---

## 📊 Datos Persistentes

### `datos/usuarios.json`
Archivo JSON con lista de usuarios del sistema.

**Formato:**
```json
[
  {
    "identificacion": "12345",
    "nombre": "Juan Pérez",
    "password": "pass123"
  },
  {
    "identificacion": "67890",
    "nombre": "María García",
    "password": "pass456"
  }
]
```

### `datos/productos.json`
Archivo JSON con catálogo de productos del restaurante.

**Formato:**
```json
[
  {
    "codigo": "P001",
    "nombre": "Pizza Margherita",
    "precio": 12.50,
    "stock": 10
  },
  {
    "codigo": "P002",
    "nombre": "Hamburguesa",
    "precio": 8.99,
    "stock": 25
  }
]
```

---

## 🚀 Cómo Usar la Aplicación

### 1. Iniciar la aplicación
```bash
python main.py
```

### 2. Pantalla de Login
- Ingrese un ID de usuario (ej: "12345")
- Ingrese la contraseña asociada (ej: "pass123")
- Haga clic en "Ingresar"

### 3. Pantalla Principal - Pestaña Usuarios
- Visualice la lista de todos los usuarios registrados en el sistema
- Esta información es de solo lectura (visualización)

### 4. Pantalla Principal - Pestaña Productos
**Registrar un nuevo producto:**
- Ingrese código (ej: "P003")
- Ingrese nombre (ej: "Ensalada César")
- Ingrese precio (ej: "7.99")
- Ingrese stock (ej: "15")
- Haga clic en "Registrar"

**Consultar un producto:**
- Ingrese el código del producto
- Haga clic en "Consultar"
- Se mostrará ventana con información del producto

**Actualizar un producto:**
- Ingrese el código y los nuevos datos
- Haga clic en "Actualizar"

**Eliminar un producto:**
- Ingrese el código del producto
- Haga clic en "Eliminar"

### 5. Cerrar sesión
- Haga clic en el botón "Cerrar sesión"
- Retornará a la pantalla de login

---

## 🔐 Validaciones y Manejo de Errores

### Validaciones de Usuario:
✅ ID debe ser numérico  
✅ Nombre no puede estar vacío  
✅ Contraseña no puede estar vacía  
✅ Credenciales deben coincidir exactamente  

### Validaciones de Producto:
✅ Código no puede estar vacío  
✅ Precio debe ser mayor a 0  
✅ Stock no puede ser negativo  
✅ No se permite código duplicado  
✅ No se puede vender más que stock disponible  

### Manejo de Excepciones:
- Archivos JSON no encontrados: retorna lista vacía
- JSON inválido: muestra mensaje de error
- Errores de permisos: informa al usuario
- Operaciones inválidas: muestra messagebox con descripción del error

---

## 💾 Persistencia de Datos

- Todos los cambios en productos se guardan **automáticamente** en `productos.json`
- Los usuarios se cargan al iniciar pero **no se pueden modificar desde la UI**
- Cada operación de actualización/eliminación de productos persiste inmediatamente
- Los datos sobreviven al cerrar y reabrir la aplicación

---

## 🏗️ Arquitectura y Patrones

### Patrón MVC (Modelo-Vista-Controlador):
- **Modelo**: Clases `Usuario` y `Producto` (modelos/)
- **Vista**: `LoginView` y `MainView` (ui/)
- **Controlador**: `RestauranteServicio` (servicios/)

### Inyección de Dependencias:
- Las vistas reciben el servicio como parámetro
- Las vistas reciben callbacks para navegar entre pantallas
- Desacoplamiento entre componentes

### Patrón Singleton (ArchivoServicio):
- Métodos estáticos para operaciones de archivo
- No requiere instanciación

### Separación de Responsabilidades:
- Modelos: Validación de datos y representación
- Servicios: Lógica de negocio y persistencia
- Vistas: Interfaz gráfica e interacción usuario
- Aplicación: Orquestación y navegación

---

## 🔄 Flujo de Datos

```
┌─────────────────────────────────────────────────────────────┐
│                   APLICACION (main.py)                      │
│  ┌─────────────────────────────────────────────────────────┐│
│  │ Carga usuarios.json y productos.json                    ││
│  └─────────────────────────────────────────────────────────┘│
│                          ↓                                    │
│  ┌─────────────────────────────────────────────────────────┐│
│  │        RESTAURANTE_SERVICIO (servicios/)                 ││
│  │ - Gestiona usuarios y productos en memoria               ││
│  │ - Persiste en JSON mediante ArchivoServicio              ││
│  └─────────────────────────────────────────────────────────┘│
│       ↑                                    ↑                 │
│       │ Datos/Validación                  │ Datos/Validación│
│       │                                    │                 │
│  ┌──────────┐                      ┌──────────────┐          │
│  │  USUARIO │                      │  PRODUCTO    │          │
│  │ (modelos)│                      │  (modelos)   │          │
│  └──────────┘                      └──────────────┘          │
│       ↑                                    ↑                 │
│       └────────────────┬────────────────────┘                │
│                        │ Visualización                       │
│  ┌─────────────────────┴─────────────────────┐              │
│  │           MAIN_VIEW (ui/)                  │              │
│  │  ┌──────────────┬──────────────────────┐  │              │
│  │  │   Usuarios   │   Productos (CRUD)   │  │              │
│  │  └──────────────┴──────────────────────┘  │              │
│  └──────────────────────────────────────────┘              │
│  ┌──────────────────────────────────────────┐              │
│  │       LOGIN_VIEW (ui/)                    │              │
│  │  Autenticación contra RestauranteServicio│              │
│  └──────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Ejemplo de Uso Completo

### Crear usuario administrador (manual):
```json
// En datos/usuarios.json, agregar:
{
  "identificacion": "1001",
  "nombre": "Admin",
  "password": "admin123"
}
```

### Crear producto inicial (manual):
```json
// En datos/productos.json, agregar:
{
  "codigo": "BEBIDA001",
  "nombre": "Agua Mineral 500ml",
  "precio": 2.50,
  "stock": 100
}
```

### Ejecutar:
```bash
$ python main.py
# La ventana se abre con LoginView
# Ingrese: ID=1001, Password=admin123
# Click en "Ingresar"
# Aparece MainView con tabla de usuarios y gestión de productos
```

---

## 🛠️ Requisitos del Sistema

- **Python**: 3.6+
- **Tkinter**: Incluido en Python (generalmente preinstalado)
- **Sistema Operativo**: Windows, macOS, Linux

### Dependencias:
```
- tkinter (estándar)
- json (estándar)
```

---

## 📌 Notas Importantes

1. **Contraseñas**: En producción, las contraseñas deben estar encriptadas, no en texto plano
2. **Usuarios**: La aplicación actual no permite crear usuarios desde la UI (solo cargar de JSON)
3. **Archivos JSON**: Deben estar en la ruta especificada (`restaurante_app/datos/`)
4. **Identificaciones**: Deben ser numéricas (validación de la clase Usuario)
5. **Tabla de Productos**: Se actualiza automáticamente al registrar, actualizar o eliminar

---

## 👨‍💻 Autor

**José Luna** - Parcial 2, Semana 14 - Programación Orientada a Objetos

---

## 📄 Licencia

Este proyecto es de uso educativo.

---

## 🆘 Solución de Problemas

### "FileNotFoundError: productos.json"
- Verifique que el archivo existe en `restaurante_app/datos/productos.json`
- Verifique los permisos de lectura de la carpeta `datos/`

### "Credenciales inválidas"
- Verifique que la identificación sea numérica
- Asegúrese de que usuario/contraseña coincidan exactamente en `usuarios.json`
- Recuerde que es case-sensitive

### "El precio debe ser mayor a 0"
- Ingrese un valor decimal válido (ej: 10.50, 5.99)
- No ingrese valores negativos o cero

### "Stock insuficiente"
- Esta validación está en la clase Producto
- No se puede vender más cantidad que la disponible

---

## 🔔 Changelog

**v1.0** (Semana 14)
- Implementación inicial de Restaurante App
- Autenticación de usuarios
- CRUD completo de productos
- Persistencia en JSON
- Interfaz gráfica con Tkinter
