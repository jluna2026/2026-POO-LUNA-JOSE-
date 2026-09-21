import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, root, servicio, callback_logout):
        super().__init__(root)
        self.servicio = servicio
        self.callback_logout = callback_logout

        # Contenedor principal con pestañas
        contenedor = ttk.Notebook(self)
        contenedor.pack(fill="both", expand=True)

        # Sección Usuarios
        frame_usuarios = ttk.Frame(contenedor)
        contenedor.add(frame_usuarios, text="Usuarios")
        self._crear_seccion_usuarios(frame_usuarios)

        # Sección Productos
        frame_productos = ttk.Frame(contenedor)
        contenedor.add(frame_productos, text="Productos")
        self._crear_seccion_productos(frame_productos)

        # Botón de cerrar sesión
        ttk.Button(self, text="Cerrar sesión", command=self.callback_logout).pack(pady=10)

    # ---------------- USUARIOS ----------------
    def _crear_seccion_usuarios(self, frame):
        ttk.Label(frame, text="Consulta de usuarios", font=("Arial", 12, "bold")).pack(pady=10)

        tabla = ttk.Treeview(frame, columns=("id", "nombre"), show="headings")
        tabla.heading("id", text="Identificación")
        tabla.heading("nombre", text="Nombre")
        tabla.pack(fill="both", expand=True)

        # Cargar usuarios desde servicio
        for u in self.servicio.listar_usuarios():
            tabla.insert("", "end", values=(u.identificacion, u.nombre))

    # ---------------- PRODUCTOS ----------------
    def _crear_seccion_productos(self, frame):
        ttk.Label(frame, text="Gestión de productos", font=("Arial", 12, "bold")).pack(pady=10)

        # Formulario
        form = ttk.Frame(frame)
        form.pack(pady=5)

        ttk.Label(form, text="Código").grid(row=0, column=0, sticky="w")
        self.codigo_entry = ttk.Entry(form)
        self.codigo_entry.grid(row=0, column=1)

        ttk.Label(form, text="Nombre").grid(row=1, column=0, sticky="w")
        self.nombre_entry = ttk.Entry(form)
        self.nombre_entry.grid(row=1, column=1)

        ttk.Label(form, text="Precio").grid(row=2, column=0, sticky="w")
        self.precio_entry = ttk.Entry(form)
        self.precio_entry.grid(row=2, column=1)

        ttk.Label(form, text="Stock").grid(row=3, column=0, sticky="w")
        self.stock_entry = ttk.Entry(form)
        self.stock_entry.grid(row=3, column=1)

        # Botones de acción
        acciones = ttk.Frame(frame)
        acciones.pack(pady=10)

        ttk.Button(acciones, text="Registrar", command=self._registrar_producto).grid(row=0, column=0, padx=5)
        ttk.Button(acciones, text="Consultar", command=self._consultar_producto).grid(row=0, column=1, padx=5)
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_producto).grid(row=0, column=2, padx=5)
        ttk.Button(acciones, text="Eliminar", command=self._eliminar_producto).grid(row=0, column=3, padx=5)

        # Tabla de productos
        self.tabla_productos = ttk.Treeview(frame, columns=("codigo", "nombre", "precio", "stock"), show="headings")
        for col in ("codigo", "nombre", "precio", "stock"):
            self.tabla_productos.heading(col, text=col.capitalize())
        self.tabla_productos.pack(fill="both", expand=True)

        self._actualizar_tabla()

    # ---------------- MÉTODOS DE PRODUCTOS ----------------
    def _registrar_producto(self):
        try:
            codigo = self.codigo_entry.get()
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            stock = int(self.stock_entry.get())
            self.servicio.registrar_producto(codigo, nombre, precio, stock)
            self._actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto registrado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _consultar_producto(self):
        codigo = self.codigo_entry.get()
        producto = self.servicio.consultar_producto(codigo)
        if producto:
            messagebox.showinfo("Consulta", f"Producto: {producto.nombre}\nPrecio: {producto.precio}\nStock: {producto.stock}")
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def _actualizar_producto(self):
        try:
            codigo = self.codigo_entry.get()
            nombre = self.nombre_entry.get()
            precio = float(self.precio_entry.get())
            stock = int(self.stock_entry.get())
            self.servicio.actualizar_producto(codigo, nombre, precio, stock)
            self._actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _eliminar_producto(self):
        try:
            codigo = self.codigo_entry.get()
            self.servicio.eliminar_producto(codigo)
            self._actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _actualizar_tabla(self):
        # Limpiar tabla
        for row in self.tabla_productos.get_children():
            self.tabla_productos.delete(row)

        # Insertar productos actualizados
        for p in self.servicio.listar_productos():
            self.tabla_productos.insert("", "end", values=(p.codigo, p.nombre, p.precio, p.stock))
