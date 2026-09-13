import *kinter as tk

class MainView(tk.Fr*me):

    def __init__(self, maste*, servicio, callback_logout):
    *   super().__init__(master)

     *  self.servicio = servicio
       *self.callback_logout = callback_lo*out

        tk.Label(
           *self,
            text="RESTAURANT* APP",
            font=("Arial", *6, "bold")
        ).pack(pady=10)*
        tk.Button(
            se*f,
            text="Mostrar Produ*tos",
            command=self.mos*rar_productos
        ).pack(pady=*)

        tk.Button(
            *elf,
            text="Mostrar Usu*rios",
            command=self.mo*trar_usuarios
        ).pack(pady=*)

        tk.Button(
            *elf,
            text="Ventas (Pen*iente)"
        ).pack(pady=5)

  *     tk.Button(
            self,
*           text="Cerrar sesión",
 *          command=self.callback_lo*out
        ).pack(pady=20)

     *  self.area_texto = tk.Text(self, *idth=50, height=10)
        self.a*ea_texto.pack()

    def mostrar_p*oductos(self):

        self.area_*exto.delete("1.0", tk.END)

      * for producto in self.servicio.lis*ar_productos():
            self.a*ea_texto.insert(
                t*.END,
                f"{producto.*ombre} - Cantidad: {producto.canti*ad}\n"
            )

    def most*ar_usuarios(self):

        self.a*ea_texto.delete("1.0", tk.END)

  *     for usuario in self.servicio.*istar_usuarios():
            self*area_texto.insert(
                tk.END,
                f"{usuario.usuario}\n"
            )