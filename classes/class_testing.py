class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def speak(self):
        return f"Animal {self.name}"


class Pet:
    def __init__(self, owner):
        self.owner = owner


class Dog(Animal, Pet):
    def __init__(self, name, legs, owner):
        Animal.__init__(self, name, legs)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} barks"


pet = Dog('Max', 4, 'Sean')
print(pet.owner)
print(pet.speak())
