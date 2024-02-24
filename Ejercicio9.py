# Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.

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
mi_cuenta = CuentaBancaria("31124875679", ["Samuel", "Melisa"], 775000.00)
mi_cuenta.retirar(500000.00)