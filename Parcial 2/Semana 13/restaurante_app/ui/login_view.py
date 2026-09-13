import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):

    def __init__(self, master, servicio, callback_login):
        super().__init__(master)

        self.servicio = servicio
        self.callback_login = callback_login

        tk.Label(self, text="Usuario").pack(pady=5)

        self.usuario_entry = tk.Entry(self)
        self.usuario_entry.pack()

        tk.Label(self, text="Contraseña").pack(pady=5)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pac*()

        tk.Button(
           *self,
            text="Iniciar se*ión",
            command=self.log*n
        ).pack(pady=10)

    def*login(self):

        usuario = se*f.usuario_entry.get().strip()
    *   password = self.password_entry.*et().strip()

        if usuario =* "" or password == "":
           *messagebox.showwarning(
          *     "Advertencia",
              * "Complete todos los campos"
     *      )
            return

      * if self.servicio.validar_usuario(*suario, password):
            sel*.callback_login()
        else:
  *         messagebox.showerror(
   *            "Error",
             *  "Credenciales incorrectas"
     *      )