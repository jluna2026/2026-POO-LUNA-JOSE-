import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Frame):
    def __init__(self, root, servicio, callback_principal):
        super().__init__(root)
        self.servicio = servicio
        self.callback_principal = callback_principal

        # Etiquetas y entradas
        ttk.Label(self, text="Identificación").pack(pady=5)
        self.ident_entry = ttk.Entry(self)
        self.ident_entry.pack()

        ttk.Label(self, text="Contraseña").pack(pady=5)
        self.pass_entry = ttk.Entry(self, show="*")
        self.pass_entry.pack()

        # Botón de login
        ttk.Button(self, text="Ingresar", command=self._login).pack(pady=10)

    def _login(self):
        ident = self.ident_entry.get()
        password = self.pass_entry.get()
        if self.servicio.validar_usuario(ident, password):
            # Si las credenciales son correctas, llamamos al callback
            self.callback_principal()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")
