# 🍽️ Sistema de Gestión de Restaurante

## ¿Qué hace este programa?

Este es un programa que simula un **sistema para administrar un restaurante**. Te permite guardar información sobre:

- **Productos/Platillos**: Los platos que ofrece el restaurante (nombre, código, categoría y precio)
- **Bebidas**: Las bebidas especiales del restaurante (igual que los platillos pero con un tamaño)
- **Clientes**: Las personas que visitan el restaurante (nombre, identificación y correo)

## 📋 Funciones principales

El programa tiene un menú interactivo con las siguientes opciones:

1. **Registrar producto**: Añade un nuevo platillo al restaurante
2. **Registrar bebida**: Añade una nueva bebida al restaurante
3. **Registrar cliente**: Guarda los datos de un nuevo cliente
4. **Listar productos**: Muestra todos los platillos y bebidas registrados
5. **Listar clientes**: Muestra todos los clientes registrados
6. **Salir**: Cierra el programa

## 🚀 Cómo usar el programa

1. **Abre la terminal** en la carpeta del proyecto
2. **Ejecuta** el comando:
   ```
   python main.py
   ```
3. **Sigue el menú**: Selecciona una opción escribiendo su número (1, 2, 3, 4, 5 o 6)
4. **Completa los datos**: Cuando el programa te pida información, escribe los datos y presiona Enter

## 📝 Ejemplo de uso

```
1. Selecciona "1" para registrar un producto
2. Escribe: Código: P001
3. Escribe: Nombre: Pizza Margherita
4. Escribe: Categoría: Italiana
5. Escribe: Precio: 12.50
6. El producto se guarda automáticamente
7. Selecciona "4" para ver todos los productos registrados
```

## 📁 Estructura del programa

- **main.py**: El programa principal con el menú
- **modelos/**: Carpeta con las clases (Producto, Bebida, Cliente)
- **servicios/**: Carpeta con la lógica del restaurante

## 💡 Notas importantes

- ⚠️ Los datos se almacenan solo mientras el programa está abierto (al cerrarlo se pierden)
- ✅ No se pueden registrar dos clientes con la misma identificación
- 💰 Los precios se muestran con 2 decimales

