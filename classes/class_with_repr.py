class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self.model}, {self.year})'

    def __str__(self):
        return f'A {self.year} {self.model}'


mustang = Car('Shelby', 1967)
