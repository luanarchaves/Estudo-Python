class Carro():
    def __init__(self, modelo, cor, velocidade):
        self.modelo = modelo
        self.cor = cor 
        self.velocidade = velocidade

    def Acelerar(self):
        print("O carro esta acelerando!")

        i = 0
        while (i <= self.velocidade):
            print (f"acelerando: {i}KM/H")
            i += 10


    def Frear(self):
        print("Carro esta desacelerando")

        i = self.velocidade
        while (i >= 0):
            print(f"freando: {i}")
            i -= 10

carro = Carro("Sedan", "Branco", 120)

carro.Acelerar()
carro.Frear()