import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio

from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:

    def __init__(self, root):

        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("500x450")

        archivo_servicio = ArchivoServicio()

        productos = archivo_servicio.leer_json(
            "datos/productos.json"
        )

        usuarios = archivo_servicio.leer_json(
            "datos/usuarios.json"
        )

        self.restaurante_servicio = RestauranteServicio(
            productos,
            usuarios
        )

        self.mostrar_login()

    def limpiar_ventana(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):

        self.limpiar_ventana()

        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_principal
        )

        vista.pack(fill="both", expand=True)

    def mostrar_principal(self):

        self.limpiar_ventana()

        vista = MainView(
            self.root,
            self.restaurante_servio,
            self.mostrar_login
        )

        vista.pack(fill="both", expand=True)


if __name__ == "__main__":

    ventana = tk.Tk()

    app = Aplicacion(ventana)

    ventana.mainloop()