#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def perimetro(self):
        ancho = abs(self.esquina1[0] - self.esquina2[0])
        alto = abs(self.esquina1[1] - self.esquina2[1])
        return 2 * (ancho + alto)

    def area(self):
        ancho = abs(self.esquina1[0] - self.esquina2[0])
        alto = abs(self.esquina1[1] - self.esquina2[1])
        return ancho * alto

    def es_cuadrado(self):
        ancho = abs(self.esquina1[0] - self.esquina2[0])
        alto = abs(self.esquina1[1] - self.esquina2[1])
        return ancho == alto

# Ejemplo de uso
rectangulo = Rectangulo((0, 0), (2, 2))

print("Perímetro:", rectangulo.perimetro())
print("Área:", rectangulo.area())
print("¿Es un cuadrado?", rectangulo.es_cuadrado())