from restaurante_app.modelos.platillo import Platillo
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.servicios.restaurante import Restaurante

def main():
    restaurante = Restaurante("La Tía Lea")

    # Crear objetos
    platillo1 = Platillo("Arroz con pollo", 3.50, 600)
    platillo2 = Platillo("Ceviche", 4.00, 450)
    bebida1 = Bebida("Jugo de naranja", 1.50, 300)
    bebida2 = Bebida("Coca-Cola", 1.20, 350)

    # Agregar al restaurante
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    # Mostrar menú
    restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
