import tkinter as tk

class MainView(tk.Frame):

    def __init__(self, master, servicio, callback_logout):
        super().__init__(master)

        self.servicio = servicio
        self.callback_logout = callback_logout

        tk.Label(
            self,
            text="RESTAURANTE APP",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Button(
            self,
            text="Mostrar Productos",
            command=self.mostrar_productos
        ).pack(pady=5)

        tk.Button(
            self,
            text="Mostrar Usuarios",
            command=self.mostrar_usuarios
        ).pack(pady=5)

        tk.Button(
            self,
            text="Ventas (Pendiente)"
        ).pack(pady=5)

        tk.Button(
            self,
            text="Cerrar sesión",
            command=self.callback_logout
        ).pack(pady=10)

        self.area_texto = tk.Text(self, width=50, height=10)
        self.area_texto.pack(pady=10)

    def mostrar_productos(self):
        self.area_texto.delete("1.0", tk.END)

        for producto in self.servicio.listar_productos():
            self.area_texto.insert(
                tk.END,
                f"{producto.nombre} - Cantidad: {producto.cantidad}\n"
            )

    def mostrar_usuarios(self):
        self.area_texto.delete("1.0", tk.END)

        for usuario in self.servicio.listar_usuarios():
            self.area_texto.insert(
                tk.END,
                f"{usuario.usuario}\n"
            )