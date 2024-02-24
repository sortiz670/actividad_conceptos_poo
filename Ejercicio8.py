# Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print("Se depositaron", cantidad, "en la cuenta.")
        print("Nuevo balance:", self.balance)
mi_cuenta = CuentaBancaria("31124875679", ["Samuel", "Melisa"], 275000.00)
mi_cuenta.depositar(500000.00)