from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass
    
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
def resultado(FormaGeometrica):
    print(f"{FormaGeometrica.calcular_area()}")
    print(f"{FormaGeometrica.calcular_perimetro()}")
    
    
retangulo = Retangulo(5, 2)
resultado(retangulo)
circulo = Circulo(5)
resultado(circulo)

