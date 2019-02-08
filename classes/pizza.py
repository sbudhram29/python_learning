from math import pi


class Pizza:
    '''
    Testing out classmethod and staticmethod
    using a Pizza example
    '''

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    def __repr__(self):
        return f"{__class__.__name__}({self.ingredients})"

    def __str__(self):
        ingredients = ", " .join(self.ingredients)
        return f"A {__class__.__name__} with {ingredients}"

    '''
    classmethods are useds to create predefine instance of
    the class
    '''
    @classmethod
    def Cheese(cls):
        return cls(['cheese'])

    @classmethod
    def Pepperoni(cls):
        return cls(['cheese', 'pepperoni'])

    '''
    staticmethods are useds to create methond that can be
    accessed without a class instance and doesn't effect
    the class
    '''
    @staticmethod
    def area(r):
        return 2*pi*r


print(Pizza.Cheese())
print(Pizza.Pepperoni())
print(Pizza.area(16))
