class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico
        
    def encender(self) -> str:
        return f"El electrodoméstico {self.marca} {self.modelo} está encendido y consume {self.consumoEnergetico} kw."

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, capacidad: float):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad
    
    def encender(self) -> str:
        return f"La lavadora {self.marca} {self.modelo} con capacidad de {self.capacidad} kg está encendida y consume {self.consumoEnergetico} kw."
    
    def iniciarCicloDeLavado(self) -> str:
        return "La lavadora ha iniciado un ciclo de lavado."


class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, tieneCongelador: bool):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador
    
    def encender(self) -> str:
        tipo = "con congelador" if self.tieneCongelador else "sin congelador"
        return f"El refrigerador {self.marca} {self.modelo} {tipo} está encendido y consume {self.consumoEnergetico} kw."
    
    def regularTemperatura(self) -> str:
        return "El refrigerador está regulando la temperatura."


lavadora1 = Lavadora("LG", "Turbo", 1.5, 10)
refrigerador1 = Refrigerador("Samsung", "Cool", 0.9, True)
print(lavadora1.encender())
print(lavadora1.iniciarCicloDeLavado())
print(refrigerador1.encender())
print(refrigerador1.regularTemperatura())

