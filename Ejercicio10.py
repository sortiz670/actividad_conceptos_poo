# Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Se depositaron", cantidad, "en la cuenta.")
        print("Nuevo balance:", self.balance)

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("No se puede retirar. Fondos insuficientes.")
        else:
            self.balance -= cantidad
            print("Se retiraron", cantidad, "de la cuenta.")
            print("Nuevo balance:", self.balance)

    def aplicar_cuota_manejo(self):
        cuota_manejo = self.balance * 0.02
        self.balance -= cuota_manejo
        print("Se aplicó una cuota de manejo del 2% sobre el balance.")
        print("Nuevo balance después de aplicar la cuota de manejo:", self.balance)
mi_cuenta = CuentaBancaria("31124875679", ["Samuel", "Melisa"], 275000.00)
mi_cuenta.aplicar_cuota_manejo()