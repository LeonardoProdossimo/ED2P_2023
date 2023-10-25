import math

class Circulo:
    def __init__(self, x, y, raio):
        self.x = x  
        self.y = y  
        self.raio = raio  

    def calcular_area(self):
        return math.pi * self.raio**2

    def calcular_diametro(self):
        return 2 * self.raio

    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

    def mudar_posicao(self, novo_x, novo_y):
        self.x = novo_x
        self.y = novo_y

    def __str__(self):
        return f"Círculo de raio {self.raio} no ponto ({self.x}, {self.y})"

# Exemplo de uso da classe Circulo
circulo = Circulo(3, 4, 5)  
print(circulo)  # Exibe informações sobre o círculo
print(f"Área: {circulo.calcular_area()}")
print(f"Diâmetro: {circulo.calcular_diametro()}")
print(f"Circunferência: {circulo.calcular_circunferencia()}")

# Muda a posição do círculo para (1, 2)
circulo.mudar_posicao(1, 2)
print(circulo)  