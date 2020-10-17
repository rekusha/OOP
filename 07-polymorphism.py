print(1+1)
print('1'+'2')
print(['1']+['2', 3])
print(tuple('1')+tuple('2'))
print('1'.__add__('2'))  # + это синтаксический сахар для метода __add__
print('--------------')
# полиморфизм, это использование одного метода для разных типов данных с получением разного результата и поведения


class Person:
    age = 1

    def __add__(self, other):
        self.age += 1
        return self.age


a = Person()
a + 100
print(str(a.age))
a + '12d'
print(str(a.age))
# что бы не прибавляли, занчение будет увеличиваться на 1 потому как переопределен метод __add__

# логика поиска одна, сначало ищем в экземпляре класса, затем в классе, после у предков в конце глоб. классе object
print('--------------')


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError('Wrong pbject')

    def __eq__(self, room_obj):
        if isinstance(room_obj, Room):
            if self.area == room_obj.area:
                return True
            else:
                return False
        raise TypeError('Wrong pbject')


r1 = Room(3, 5)
r2 = Room(4, 7)
r3 = Room(5, 3)
print(r1+r2)
print(r1 == r2)
print(r1 == r3)

