class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.floors + value)
        return NotImplemented

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, value + self.floors)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented
