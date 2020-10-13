class Person:
    def __init__(self, name, surename):
        self._name = name  # fore 1th and 2th part
        self._surename = surename  # fore 2th part
        self._full_name = None  # fore 3th part (cache)

    # @property  # если не создавать свойства сеттер то этот атрибут будет только для чтения ))
    # def name(self):
    #     return self._name

    @property  # если не создавать свойства сеттер то этот атрибут будет только для чтения ))
    def full_name(self):
        if self._full_name is None:  # если кэш None, пересчитать кэш
            self._full_name = f'{self._name} {self._surename}'
        return self._full_name  # вернуть кэш

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None  # 3 при изменении имени или фамилии установить кэш в None

    @property
    def surename(self):
        return self._surename

    @surename.setter
    def surename(self, value):
        self._surename = value
        self._full_name = None  # 3 при изменении имени или фамилии установить кэш в None


p = Person('Ivan', 'Ivanoff')
print(p.full_name)
print(p)
p.surename = 'Petroff'
print(p.full_name)
print(p)
# вычисляемые свойства вычесляются как в p.full_name, даже если иванов сменит фамилию, то нет смысла менять объект,
# а просто стоит сменить фамилию и у того же объекта будет новая фамилия

# кеширование: используется для того чтобы уменьшить накладные расходы. кэш хранит в себе результат вычисления и отдает
# его по требованию без вычислений, кэш изменяется лишь тогда, когда вычисляемые свойства изменяются
print('--------------')
p = Person('Ivan', 'Ivanoff')
print(p.__dict__, 'cache is None')  # нет кэша
print(p.full_name+',', 'calculate cache and return it')  # нет кэша - вычислить кэш и занести в переменную - вернуть кэш
print(p.__dict__, 'cache is "Ivan Ivanoff"')  # кэш есть
p.surename = 'Petroff'  # меняем фамилию сбрасывая кэш в None
print(p.__dict__, 'cache is None')
print(p.full_name+',', 'calculate cache and return it')  # нет кэша - вычислить новый кэш и занести в переменную - вернуть кэш
print(p.__dict__, 'cache is "Ivan Petroff"')
