# =====================================================================
# Tarea Semana 2: Técnicas de Programación (POO en Python)
# Concepto: Representación de un objeto del mundo real (Cuenta Bancaria)
# =====================================================================

# 1. Definición de la Clase (plantilla)
class CuentaBancaria:

    # Método constructor: Define los atributos iniciales del objeto
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular  # Atributo: Nombre del dueño de la cuenta
        self.saldo = saldo_inicial  # Atributo: Dinero disponible

    # Método para mostrar el estado de la cuenta
    def mostrar_informacion(self):
        print(f"\n--- Estado de Cuenta ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo disponible: ${self.saldo:.2f}")
        print("------------------------")

    # Método para depositar dinero (Comportamiento)
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"✔ Depósito exitoso: Se han abonado ${monto:.2f} a la cuenta.")
        else:
            print("❌ Error: El monto a depositar debe ser mayor a cero.")

    # Método para retirar dinero (Comportamiento con validación)
    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"✔ Retiro exitoso: Se han retirado ${monto:.2f}.")
            else:
                print(f"❌ Error: Fondos insuficientes. Intenta un monto menor a ${self.saldo:.2f}.")
        else:
            print("❌ Error: El monto a retirar debe ser mayor a cero.")


# =====================================================================
# 2. Creación de Objetos y Demostración de Funcionamiento
# =====================================================================
if __name__ == "__main__":
    print("=== Simulador de Sistema Bancario (POO) ===")

    # Creación (instanciación) de un objeto de la clase CuentaBancaria
    mi_cuenta = CuentaBancaria("José Luna", 150.00)

    # Evidencia de los conceptos estudiados:

    # 1. Mostrar estado inicial
    mi_cuenta.mostrar_informacion()

    # 2. Ejecutar un depósito (Uso de métodos)
    mi_cuenta.depositar(50.50)

    # 3. Intentar un retiro mayor al saldo (Validación de lógica)
    mi_cuenta.retirar(300.00)

    # 4. Ejecutar un retiro válido
    mi_cuenta.retirar(30.00)

    # 5. Mostrar estado final para comprobar los cambios en los atributos
    mi_cuenta.mostrar_informacion()