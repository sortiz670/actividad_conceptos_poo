#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje..

class Vehiculo:
  def __init__(self, velocidad_maxima, kilometraje):
    self.velocidad_maxima = velocidad_maxima
    self.kilometraje = kilometraje
mi_vehiculo = Vehiculo(200, 50000)
print("Velocidad maxima:",mi_vehiculo.velocidad_maxima)
mi_vehiculo.velocidad_maxima
print("Kilometraje:",mi_vehiculo.kilometraje)