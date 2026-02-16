class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name
