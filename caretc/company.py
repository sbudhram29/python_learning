class Company:
    name: str
    id: int
    library: str

    def __init__(self, name, id, library):
        self.name = name
        self.id = id
        self.library = library

    def __repr__(self):
        return f"{__class__.__name__}({self.name}, {self.id}, {self.library})"


carlisle = Company('Carlisle', 1, 'acsdbase')


print(carlisle.name)
print(carlisle.id)
