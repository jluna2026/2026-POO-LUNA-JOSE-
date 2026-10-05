class Usuario:

    LONGITUD_MINIMA_CONTRASENA = 4

    ROLES_VALIDOS = (
        "Administrador",
        "Empleado",
        "Cliente"
    )

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        telefono: str,
        usuario: str,
        contrasena: str,
        rol: str = "Cliente"
    ) -> None:

        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:

        if not valor or not valor.strip():
            raise ValueError(
                "La identificacion no puede estar vacia."
            )

        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:

        if not valor or not valor.strip():
            raise ValueError(
                "El nombre no puede estar vacio."
            )

        self._nombre = valor.strip()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:

        if not valor or not valor.strip():
            raise ValueError(
                "El telefono no puede estar vacio."
            )

        if not valor.strip().isdigit():
            raise ValueError(
                "El telefono debe contener solo digitos."
            )

        self._telefono = valor.strip()

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: str) -> None:

        if not valor or not valor.strip():
            raise ValueError(
                "El nombre de usuario no puede estar vacio."
            )

        self._usuario = valor.strip().lower()

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor: str) -> None:

        if not valor or not valor.strip():
            raise ValueError(
                "La contrasena no puede estar vacia."
            )

        valor_limpio = valor.strip()

        if len(valor_limpio) < self.LONGITUD_MINIMA_CONTRASENA:
            raise ValueError(
                f"La contrasena debe tener al menos "
                f"{self.LONGITUD_MINIMA_CONTRASENA} caracteres."
            )

        if " " in valor_limpio:
            raise ValueError(
                "La contrasena no puede contener espacios."
            )

        self._contrasena = valor_limpio

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, valor: str) -> None:

        if not valor or not valor.strip():
            raise ValueError(
                "Debe seleccionar un rol."
            )

        rol = valor.strip()

        if rol not in self.ROLES_VALIDOS:
            raise ValueError(
                f"Rol invalido. "
                f"Roles permitidos: "
                f"{', '.join(self.ROLES_VALIDOS)}"
            )

        self._rol = rol

    def validar_credenciales(
        self,
        usuario: str,
        contrasena: str
    ) -> bool:

        return (
            self.usuario == usuario.strip().lower()
            and
            self.contrasena == contrasena.strip()
        )

    def es_administrador(self) -> bool:

        return self.rol == "Administrador"

    def convertir_a_diccionario(self) -> dict:

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }

    def __str__(self) -> str:

        return (
            f"Identificacion: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Telefono: {self.telefono} | "
            f"Rol: {self.rol}"
        )