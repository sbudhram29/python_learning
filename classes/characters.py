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
print(harry.__class__)
print(harry.__repr__)
print(harry.__str__)
print(harry.__init__)


def combiner(list_of_items):
    str_result = ""
    num_result = 0

    for item in list_of_items:
        if isinstance(item, (str)):
            str_result += str(item)
        if isinstance(item, (float, int)):
            num_result += item

    return str_result + str(num_result) if num_result else str_result


print(combiner(["apple", "dog"]))


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        result = ""
        for i in self.pattern:
            if len(result):
                result += '-'
            if i == '.':
                result += 'dot'
            if i == '_':
                result += 'dash'
        return result


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


s = S()

print(s.__str__())


class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


str = ReversedStr('olleh')
print(str)
