# tradicional.py
# Programa de gestión de mascotas con programación tradicionala

def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    return {"nombre": nombre, "especie": especie, "edad": edad}

def mostrar_mascota(mascota):
    print("\n--- Información de la Mascota ---")
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad: {mascota['edad']} años")

# Programa principal
mascota = registrar_mascota()
mostrar_mascota(mascota)