import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class LoginView(tk.Frame):

    def __init__(self, master, restaurante_servicio, callback_login):
        super().__init__(master, bg="#eef3f8")

        self.restaurante_servicio = restaurante_servio = restaurante_servicio
        self.callback_login = callback_login

        self.usuario_entry = None
        self.password_entry = None
        self.mensaje_error = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except:
            pass

        estilo.configure(
            "Login.TButton",
            font=("Arial", 11, "bold"),
            padding=(14, 8)
        )

    def construir_interfaz(self):

        contenedor = tk.Frame(
            self,
            bg="#ffffff",
            padx=30,
            pady=25
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        titulo = tk.Label(
            contenedor,
            text="Restaurante App",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 22, "bold")
        )

        titulo.pack(pady=(0, 5))

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11)
        )

        subtitulo.pack(pady=(0, 20))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11)
        )

        self.usuario_entry.pack(
            pady=(4, 12),
            ipady=4
        )

        self.usuario_entry.focus()

        tk.Label(
            contenedor,
            text="Contraseña",
            bg="#ffffff",
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        self.password_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*"
        )

        self.password_entry.pack(
            pady=(4, 12),
            ipady=4
        )

        self.password_entry.bind(
            "<Return>",
            lambda event: self.login()
        )

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="red",
            font=("Arial", 10)
        )

        self.mensaje_error.pack(pady=(0, 10))

        ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.login,
            style="Login.TButton"
        ).pack(fill="x")

    def login(self):

        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if usuario == "" or password == "":

            self.mensaje_error.config(
                text="Complete todos los campos."
            )

            return

        if self.restaurante_servicio.validar_usuario(
                usuario,
                password
        ):

            self.mensaje_error.config(text="")

            self.callback_login()

        else:

            self.mensaje_error.config(
                text="Credenciales incorrectas."
            )

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )