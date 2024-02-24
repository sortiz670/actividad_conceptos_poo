# Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
mi_cuenta = CuentaBancaria("31124875679", ["Samuel", "Melisa"], 275000.00)
print("Número de cuenta:", mi_cuenta.numero_cuenta)
print("Propietarios:", mi_cuenta.propietarios)
print("Balance:", mi_cuenta.balance)