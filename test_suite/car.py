class Vehicle:
    def __init__(self, wheel):
        self.wheel = wheel

    def __str__(self):
        return f"A Vehicle with {self.wheel} Wheel(s)"

    def __repr__(self):
        return f"Vehicle('{self.wheel}')"


class Car(Vehicle):
    def __init__(self, make, model, year, wheel):
        Vehicle.__init__(self, wheel)
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"A {self.year}: {self.make} with {self.wheel}"

    def __repr__(self):
        return f"Car('{self.make}', {self.year}, {self.wheel})"
