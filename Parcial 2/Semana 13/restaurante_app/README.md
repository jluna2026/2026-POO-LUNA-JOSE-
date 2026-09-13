# 🍽️ Restaurante App

Una aplicación de gestión de restaurante construida con Python y Tkinter. Permite a los usuarios autenticarse y acceder a un sistema de gestión de productos e inventario.

## 📋 Descripción General

**Restaurante App** es una aplicación de escritorio desarrollada como proyecto educativo en Programación Orientada a Objetos (POO). La aplicación implementa un sistema de login seguro y proporciona una interfaz gráfica moderna para gestionar usuarios y productos de un restaurante.

---

## ✨ Características Principales

- ✅ **Sistema de Autenticación**: Login seguro con validación de credenciales
- 📦 **Gestión de Productos**: Visualización y control de inventario
- 👥 **Gestión de Usuarios**: Sistema de usuarios registrados
- 🎨 **Interfaz Gráfica Moderna**: Interfaz amigable con Tkinter
- 💾 **Persistencia de Datos**: Datos almacenados en archivos JSON

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── main.py                          # Archivo principal de la aplicación
├── datos/                           # Carpeta con archivos de datos JSON
│   ├── usuarios.json               # Base de datos de usuarios
│   └── productos.json              # Base de datos de productos
├── modelos/                         # Modelos de datos (clases)
│   ├── __init__.py
│   ├── usuario.py                  # Clase Usuario
│   └── producto.py                 # Clase Producto
├── servicios/                       # Servicios (lógica de negocio)
│   ├── __init__.py
│   ├── archivo_servicio.py         # Servicio para leer archivos JSON
│   └── restaurante_servicio.py     # Servicio principal del restaurante
└── ui/                              # Interfaz de usuario
    ├── __init__.py
    ├── login_view.py               # Vista de login
    └── main_view.py                # Vista principal
```

---

## 🧩 Componentes Principales

### 📦 Modelos

#### **Usuario** (`modelos/usuario.py`)
Representa un usuario del sistema.
```python
class Usuario:
    def __init__(self, usuario, password):
        self.usuario      # Nombre de usuario
        self.password     # Contraseña
```

#### **Producto** (`modelos/producto.py`)
Representa un producto del restaurante.
```python
class Producto:
    def __init__(self, id, nombre, cantidad):
        self.id           # Identificador único
        self.nombre       # Nombre del producto
        self.cantidad     # Cantidad disponible
```

### 🔧 Servicios

#### **ArchivoServicio** (`servicios/archivo_servicio.py`)
Gestiona la lectura de archivos JSON.
- **leer_json(ruta)**: Lee un archivo JSON y retorna los datos

#### **RestauranteServicio** (`servicios/restaurante_servicio.py`)
Servicio principal que gestiona la lógica de negocio.
- **validar_usuario(usuario, password)**: Valida las credenciales del usuario
- **listar_productos()**: Retorna la lista de productos
- **listar_usuarios()**: Retorna la lista de usuarios

### 🖥️ Interfaz de Usuario

#### **LoginView** (`ui/login_view.py`)
Pantalla de inicio de sesión con:
- Campo de entrada para usuario
- Campo de entrada para contraseña
- Validación de campos vacíos
- Validación de credenciales
- Mensajes de error

#### **MainView** (`ui/main_view.py`)
Pantalla principal después del login con:
- Visualización de productos
- Opciones de gestión
- Botón de cierre de sesión

### 🎯 Aplicación Principal (`main.py`)

Clase `Aplicacion` que:
1. Inicializa la ventana principal de Tkinter
2. Carga datos desde archivos JSON
3. Crea el servicio principal
4. Gestiona las vistas (Login y Principal)
5. Maneja las transiciones entre pantallas

---

## 🚀 Cómo Ejecutar

### Requisitos Previos
- Python 3.7 o superior
- Tkinter (generalmente incluido con Python)

### Pasos

1. **Navega a la carpeta del proyecto:**
```bash
cd restaurante_app
```

2. **Ejecuta la aplicación:**
```bash
python main.py
```

3. **Inicia sesión con las credenciales disponibles en `datos/usuarios.json`**

---

## 📊 Archivos de Datos

### `datos/usuarios.json`
Contiene la lista de usuarios registrados:
```json
[
  {
    "usuario": "admin",
    "password": "123456"
  }
]
```

### `datos/productos.json`
Contiene el inventario de productos:
```json
[
  {
    "id": 1,
    "nombre": "Pizza Margarita",
    "cantidad": 10
  }
]
```

---

## 🎓 Conceptos POO Implementados

- **Encapsulación**: Atributos privados en clases
- **Herencia**: LoginView y MainView heredan de `tk.Frame`
- **Modularidad**: Separación en capas (Modelos, Servicios, UI)
- **Abstracción**: Servicios que encapsulan la lógica de negocio
- **Composición**: Uso de objetos dentro de otros objetos

---

## 🔐 Seguridad

**Nota Importante**: Esta es una aplicación educativa. En producción, se deben implementar:
- Hash de contraseñas (bcrypt, argon2)
- Almacenamiento seguro en base de datos
- Validación adicional en el servidor
- Encriptación de datos sensibles

---

## 📝 Autor

**José Luna**  
Parcial 2 - Semana 13  
Programación Orientada a Objetos - 2026

---

## 📄 Licencia

Proyecto educativo - Libre para uso académico.

