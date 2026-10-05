# Restaurante Casero - Aplicación de Gestión

## 📋 Descripción General

**Restaurante Casero** es una aplicación de escritorio desarrollada en Python usando **Tkinter** que proporciona un sistema completo de gestión para un restaurante. La aplicación permite administrar usuarios, productos del menú, y registrar ventas realizadas en el establecimiento.

## 🎯 Objetivo del Proyecto

Este proyecto implementa una solución de software siguiendo principios de **Programación Orientada a Objetos (POO)**, demostrando el uso de:
- Modelado de datos mediante clases
- Servicios de negocio
- Interfaces gráficas con Tkinter
- Persistencia de datos con archivos JSON
- Autenticación y control de acceso

## 📁 Estructura del Proyecto

```
restaurante_app/
├── main.py                      # Punto de entrada de la aplicación
├── README.md                    # Este archivo
├── assets/                      # Recursos visuales
│   └── logo/
│       └── icono.png           # Icono de la aplicación
├── datos/                       # Archivos de datos persistentes
│   ├── productos.json          # Catálogo de productos
│   ├── usuarios.json           # Base de datos de usuarios
│   └── ventas.json             # Registro de transacciones
├── modelos/                     # Clases de dominio
│   ├── __init__.py
│   ├── usuario.py              # Modelo de usuario
│   ├── producto.py             # Modelo de producto
│   └── venta.py                # Modelo de venta
├── servicios/                   # Lógica de negocio
│   ├── __init__.py
│   ├── archivo_servicio.py     # Manejo de archivos JSON
│   └── restaurante_servicio.py # Orquestación de operaciones
└── ui/                          # Interfaz gráfica (Tkinter)
    ├── __init__.py
    ├── login_view.py           # Pantalla de autenticación
    └── main_view.py            # Interfaz principal
```

## 🔧 Componentes Principales

### Modelos de Datos
- **Usuario**: Representa un empleado del restaurante con credenciales de acceso
- **Producto**: Define los artículos del menú disponibles para vender
- **Venta**: Registra cada transacción realizada (quién vendió, qué y cuándo)

### Servicios
- **ArchivoServicio**: Maneja la lectura y escritura de datos en archivos JSON
- **RestauranteServicio**: Coordina la lógica de negocio (validaciones, operaciones CRUD)

### Interfaz de Usuario
- **LoginView**: Pantalla de autenticación para acceso a la aplicación
- **MainView**: Panel principal con acceso a todas las funcionalidades

## ✨ Características Principales

✅ **Autenticación de Usuarios**
   - Inicio de sesión seguro con verificación de credenciales

✅ **Gestión de Productos**
   - Crear, consultar, actualizar y eliminar productos del menú
   - Información de precio y disponibilidad

✅ **Registro de Ventas**
   - Registrar cada venta realizada
   - Asociar ventas con usuarios específicos
   - Mantener histórico de transacciones

✅ **Gestión de Usuarios**
   - Crear y administrar cuentas de empleados
   - Control de acceso a la aplicación

✅ **Persistencia de Datos**
   - Almacenamiento en archivos JSON
   - Datos se conservan entre ejecuciones

✅ **Interfaz Gráfica Intuitiva**
   - Desarrollo con Tkinter
   - Diseño responsivo y user-friendly

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.7 o superior
- Tkinter (generalmente incluido con Python)

### Instalación
```bash
# Clonar o descargar el repositorio
cd restaurante_app

# No se requieren dependencias externas adicionales
```

### Ejecutar la Aplicación
```bash
# Desde la raíz del proyecto
python main.py
```

La aplicación abrirá una ventana con la pantalla de login. Ingrese con las credenciales de un usuario registrado.

## 📊 Flujo de la Aplicación

```
Inicio
  ↓
LoginView (Autenticación)
  ↓
¿Credenciales válidas?
  ├─ NO → Mensaje de error → LoginView
  └─ SÍ ↓
      MainView (Interfaz Principal)
        ├─ Gestión de Productos
        ├─ Registro de Ventas
        ├─ Consultas
        └─ Cerrar Sesión → LoginView
```

## 🏗️ Arquitectura

El proyecto sigue un **patrón arquitectónico en capas**:

```
┌─────────────────────────────────────┐
│  Capa de Presentación (UI)          │
│  - LoginView                         │
│  - MainView                          │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Capa de Lógica de Negocio          │
│  - RestauranteServicio              │
│  - Validaciones                     │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Capa de Acceso a Datos             │
│  - ArchivoServicio                  │
│  - Manejo de JSON                   │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Capa de Dominio (Modelos)          │
│  - Usuario                          │
│  - Producto                         │
│  - Venta                            │
└─────────────────────────────────────┘
```

## 🎓 Conceptos de POO Implementados

- **Encapsulación**: Uso de propiedades y setters para validación
- **Abstracción**: Servicios que ocultan la complejidad
- **Herencia**: Posibilidad de extender modelos
- **Polimorfismo**: Métodos como `convertir_a_diccionario()` y `__str__()`

## 📝 Archivos de Datos

Los datos se almacenan en formato JSON en la carpeta `datos/`:

- **usuarios.json**: Lista de usuarios registrados
- **productos.json**: Catálogo de productos del menú
- **ventas.json**: Registro de todas las ventas realizadas

## 🔐 Seguridad

- Validación de credenciales en el login
- Validación de datos en los modelos
- Manejo de errores mediante excepciones

## 🛠️ Desarrollo Futuro

Posibles mejoras y extensiones:
- Encriptación de contraseñas
- Base de datos relacional (SQL)
- Generación de reportes y estadísticas
- Sistema de inventario avanzado
- Historial de auditoría
- Exportación de datos a diferentes formatos

## 📄 Licencia

Este proyecto es académico, desarrollado como parte del curso de Programación Orientada a Objetos.

---

**Autor**: José Luna  
**Curso**: POO - 2026  
**Parcial**: 2 - Semana 15
