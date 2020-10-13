class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


p = Person('Alex')
print(p.name)
p.name = 'Stas'
print(p.name)