from Asiento import *
from Motor import *

class Auto:
    def __init__(self, modelo, precio, asientos,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = [Asiento]
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados
    def cantidadAsientos(self, asientos):
        cantidadAsientos= len(asientos)
    
    def verificarIntegridad(self, motor,asiento):
        if (motor.registro==self.registro):
            for i in asientos:
                if(motor.registro != Asiento.registro):
                    print("Las piezas no son originales")
            print("Auto original")
        else:
            print("Las piezas no son originales") 

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros= numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, newRegistro):
        self.registro= newRegistro
    def asignarTipo(self, newTipo):
        if(newTipo == "electrico" or "gasolina"):
            self.tipo = newTipo

class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, newColor):
        if (newColor == "rojo" or "verde" or "amarillo" or "blanco" or "negro"):
            self.color = newColor


