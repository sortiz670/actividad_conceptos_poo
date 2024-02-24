# A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def mostrar(self):
        print("Coordenadas del punto:", self)

    def mover(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y
        print("El punto ha sido movido a las nuevas coordenadas:", self)

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)
        return distancia

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

distancia = punto1.calcular_distancia(punto2)
print("La distancia entre", punto1, "y", punto2, "es:", distancia)