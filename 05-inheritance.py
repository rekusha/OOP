class Person:
    age = 0

    def hello(self):
        print('hello')


class Student(Person):
    pass


a = Student()
print(a.age)  # <- распечатает 0 потому как поле age унаследовал от предка
a.hello()  # <- распечатает hello потому как унаследовал от предка функцию hello()
print(a.__dict__)  # <- словарь экземпляра пуст потому как своих полей и методов не имеет, все унаследовано от предка
print(Student.__dict__)  # <- в словаре класса Student, age и hello() не определены
print(Person.__dict__)  # <- age и hello() в словаре класса Person
# в экземпляре класса не нашли, пошли искать в классе Student не нашли, пошли искать в родетельском классе Person инашли
# магические методы в классах наследуются от общего предка Object


class Cpu:
    pass


class IntelCpu(Cpu):
    cpu_socket = 1151
    name = 'Intel'


class I7(IntelCpu):
    pass


class I5(IntelCpu):
    pass


i5 = I5()
i7 = I7()

print(isinstance(i5, IntelCpu))  # проверяет является ли переменная i5 экземпляром класса IntelCpu и возвращает True
# потому как изинтансе проверяет всю цепочку наследования

print(type(i5))  # <class '__main__.I5'>

print(issubclass(I5, Cpu))  # True потому как они находятся в цепочке наследования и И5 является сабклассом

print(isinstance(i5, type(i7)))  # False потому как i5 не является экземпляром i7
print(issubclass(type(i5), type(i7)))  # False потому как они "братья и сестры"
# ^^^^^^^^^^^^^^^^ наследование
# ______________________________________________________________________________________________________________________
print('------------')
# перегрузка это создание в классе свойств и методов с теми же именами что и в родительском классе


class Person1:
    def hello(self):
        print('I am Person')


class Student1(Person1):
    def hello(self):
        print('I am Student')


a = Student1()
a.hello()  # I am Student <- потому как в классе определена функция hello
# на самом деле перегрузка это создание в наследнике метода с таким же именем как у предка но со своей реализацией

# ^^^^^^^^^^^^^^^^ перегрузка
# ______________________________________________________________________________________________________________________
print('------------')


class Person2:
    def hello(self):
        print('I am Person')


class Student2(Person2):
    def goodbye(self):
        print('Goodbye')


a = Student2()
a.hello()  # наследование
a.goodbye()  # расширение

# расширение это создание в дочернем классе того, чего нет в родительском и все
# ^^^^^^^^^^^^^^^^ расширение
# ______________________________________________________________________________________________________________________
print('------------')


class Person3:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')


class Student3(Person3):
    pass


a = Student3('Ivan')  # Создали экземпляр класса
a.hello()  # вызвали метод определенный в родителе, при этом родительский hello(self) в self был передан именн именно
# экземпляр класса Student3 (следование)
print(a.__dict__)  # метода нет
print(Student3.__dict__)  # метода нет
print(Person3.__dict__)  # <function Person3.__init__ at 0x00CFA8A0> метод есть

