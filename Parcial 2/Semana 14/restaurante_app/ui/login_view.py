import tkinter as tk
from tkinter import ttk
from ui.main_view import MainView

class LoginView(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Login - Restaurante App")
        self.geometry("300x200")

        ttk.Label(self, text="Identificación").pack(pady=5)
        self.ident_entry = ttk.Entry(self)
        self.ident_entry.pack()

        ttk.Label(self, text="Contraseña").pack(pady=5)
        self.pass_entry = ttk.Entry(self, show="*")
        self.pass_entry.pack()

        ttk.Button(self, text="Ingresar", command=self._login).pack(pady=10)

    def _login(self):
        ident = self.ident_entry.get()
        password = self.pass_entry.get()
        if self.servicio.validar_usuario(ident, password):
            self.destroy()
            MainView(self.servicio).mainloop()
        else:
            tk.messagebox.showerror("Error", "Credenciales inválidas")
