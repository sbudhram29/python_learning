class Character:
    def __init__(self, health=100):
        self.health = health

    def get_health(self):
        return self.health


class Wizard(Character):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def get_name(self):
        return self._name


harry = Wizard('Harry')

print(harry.get_name())
print(harry.get_health())
