# По умолчанию два объекта считаются равными, если соответствующие переменные содержат одну и ту же ссылку.
# В противном случае объекты считаются неравными.

# хеширование это приведение строки неопределенной длины к строке с определенной длиной )
# хэшируемые объекты и равенство это ключевые момент при работе со словарями и множествами
# ключем в словаре может быть лишь неизменяемый объект

import hashlib
print((hashlib.md5('Word'.encode('utf8'))).hexdigest())
print((hashlib.md5('word'.encode('utf8'))).hexdigest())
print((hashlib.md5('WOrd'.encode('utf8'))).hexdigest())
print((hashlib.md5('WoRd'.encode('utf8'))).hexdigest())
# пример работы хеширования

# идентификация ключей в словаре идет по хэшу
# объект является хэшируемым если у него ереализовам метод __hash__
# __eq__ равенство тоже должно быть реализовано потому как оно отвечает за сравнение

# Объекты считаются равными если у них одинаковый хэш

print(hash('1'))
print(hash(1))
print(hash(1) == hash('1'))


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Person):
            return True if self.name == other.name else False
        return NotImplemented  # <- если в первом сравниваемом объекте происходит проверка принадлежности к классу и
        # эта проверка не проходит, то при возврате NotImplemented компилятор проверит второй из сравниваемых объектов
        # и если у него такой проверки нет проведет сравнение по правилам второго объекта, а если получит обратно тоже
        # NotImplemented то вернет результат False


class Person2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


p1 = Person('Ivan')  # создаем объекты класса Персон с одинаковым параметром (именем)
p2 = Person('Ivan')
p3 = Person2('Ivan')

print(p1.name)

print(p1)  # <__main__.Person object at 0x01FD6D70>
print(p2)  # <__main__.Person object at 0x01FD6C50>
print(p3)  # <__main__.Person object at 0x01FD6C50>
print(p1 == p2)  # True
print(p1 == p3)  # False - объект класса персон проверит принадлежит ли второй объект тому же классу(без NotImplemented)
print(p3 == p2)  # True - персон2 не проверяет принадлежит ли объект другому классу
print(hash(p1))  # -908471236
print(hash(p2))  # -908471236
mydict = {p1: "just text"}
print(mydict.get(p1))  # just text <- по объекту класса персон используемому как ключь в словаре извлекли данные

