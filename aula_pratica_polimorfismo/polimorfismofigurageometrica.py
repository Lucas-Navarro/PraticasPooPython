import math

class FiguraGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def calcular_area(self):
        pass
    # cada um que herdar, pode modificar de qualquer forma
    
class Quadrado(FiguraGeometrica):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__(nome)
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
class Circulo(FiguraGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def calcular_area(self):
        return ((self.raio * self.raio) * math.pi)
    
quadrado = Quadrado('Quadrado', 2)
print('Área do quadrado: ', quadrado.calcular_area())

triangulo = Triangulo('Triangulo', 2, 5)
print('Área do triangulo: ', triangulo.calcular_area())

circulo = Circulo('Circulo', 5)
print('Área do circulo: ', circulo.calcular_area())