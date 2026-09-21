import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class Aplicacion:
    def __init__(self, root: object) -> None:
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("800x600")

        # Cargar datos JSON
        productos = ArchivoServicio.cargar("restaurante_app/datos/productos.json")
        usuarios = ArchivoServicio.cargar("restaurante_app/datos/usuarios.json")

        # Crear servicio principal con datos cargados
        self.restaurante_servicio = RestauranteServicio(productos, usuarios)

        # Mostrar login al iniciar
        self.mostrar_login()

    def limpiar_ventana(self):
        """Elimina todos los widgets de la ventana principal"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_ventana()
        # LoginView recibe root y servicio
        vista_login = LoginView(self.root, self.restaurante_servicio, self.mostrar_principal)
        vista_login.pack(fill="both", expand=True)

    def mostrar_principal(self):
        self.limpiar_ventana()
        # MainView recibe root y servicio
        vista_principal = MainView(self.root, self.restaurante_servicio, self.mostrar_login)
        vista_principal.pack(fill="both", expand=True)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
