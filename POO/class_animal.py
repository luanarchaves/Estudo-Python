class Animal:
    def __init__(self, animal, cor, tamanho):
        self.animal = animal
        self.cor = cor
        self.tamanho = tamanho

    def somAnimal(self):
        print("Meu animal nao tem som por que ele e um " + self.animal)


class Gato(Animal):
    def __init__(self, animal, cor, tamanho, som):
        super().__init__(animal, cor, tamanho)
        self.som = som

    def somAnimal(self):
        print(f"Meu {self.animal} disse {self.som}")


class Cachorro(Gato):
    def __init__(self, animal, cor, tamanho, som):
        super().__init__(animal, cor, tamanho, som)

    def somAnimal(self):
         super().somAnimal()
    

animal = Animal(animal= "Largatixa", cor="verde", tamanho="pequena")

animal.somAnimal()

gato = Gato(animal="Gato", cor="Preta", tamanho="pequeno", som="miau")

gato.somAnimal()

cachorro = Cachorro(animal="cachorro", cor="branco", tamanho="grande", som="au")

cachorro.somAnimal()