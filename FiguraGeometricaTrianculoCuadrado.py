class FiguraGeometrica:
    def calcularArea(self) -> float:
        pass    

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcularArea(self) -> float:
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcularArea(self) -> float:
        return self.lado * self.lado
    
cuadradito = Cuadrado(4)
triangulito = Triangulo(3, 6)
print("Área del cuadrado:", cuadradito.calcularArea())
print("Área del triángulo:", triangulito.calcularArea())

