#Cree una clase Punto que represente un punto en el plano cartesiano

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Ejemplo de uso de la clase Punto
punto1 = Punto(3, 4)
print("Coordenadas del punto:", punto1)