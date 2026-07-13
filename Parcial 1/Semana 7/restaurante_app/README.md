# Restaurante App - Semana 7

Este pequeño sistema corresponde a la práctica de la Semana 7 y modela las operaciones básicas de un restaurante en consola. Proporciona clases y servicios para representar clientes, productos (platillos y bebidas) y la lógica para gestionar pedidos y calcular cuentas.

Características principales
- Modelos:
  - `cliente.py` — Clase que representa un cliente (nombre, id, etc.).
  - `producto.py` — Clase base para productos; en semanas anteriores se extiende a `platillo` y `bebida`.
- Servicios:
  - `restaurante.py` — Contiene la lógica para gestionar el menú, tomar pedidos y calcular el total de la cuenta.
- `main.py` — Script de entrada que muestra cómo crear objetos, simular pedidos y ver el cálculo de la cuenta.

Estructura de archivos

- `main.py`  : Punto de entrada para ejecutar la demo del restaurante.
- `modelos/` : Contiene las clases modelo (`cliente.py`, `producto.py`, `platillo.py`, `bebida.py`, ...).
- `servicios/`: Contiene la implementación de la lógica operativa (`restaurante.py`).

Requisitos
- Python 3.8+ (se desarrolló y probó con Python 3.10/3.14, pero debería funcionar con versiones modernas de 3.x).
- No hay dependencias externas obligatorias; usa la biblioteca estándar.

Cómo ejecutar
1. Abrir una terminal en la carpeta `Parcial 1/Semana 7/restaurante_app/`.
2. Ejecutar:

```powershell
python main.py
```

Qué esperar
- El script `main.py` muestra ejemplos de creación de clientes y productos, agrega pedidos al restaurante y calcula la cuenta total mostrando el detalle por cliente y el total final.

Personalización y extensión
- Puede extenderse añadiendo atributos a los modelos (precio, categoría, stock),, soportar múltiples mesas, persistencia (JSON/CSV/BD) o una interfaz gráfica/HTTP.

Licencia y autor
- Proyecto educativo para la asignatura de Programación Orientada a Objetos.

