class animal():
    def __init__(self, name):
        self.name = name

class prey(animal):
        def flee(self):
            print(f"{self.name} is fleeing!!")

class predator(animal):
        def hunt(self):
            print(f"{self.name} is hunting")

class deer(prey):
        pass

class hyena(prey, predator):
        pass

hyena = hyena(f"{input("The name your wanna give to this: ")}")
hyena.hunt()