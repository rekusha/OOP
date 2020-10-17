class A2:
    def hello(self):
        print('A2')


class A1(A2):
    pass


class A3(A2):
    pass


class C1(A1, A3):
    pass


a = C1()
print(a.__class__.mro())  # 'C1' -> 'A1' -> 'A3' -> 'A2' -> 'object'
# очередность наследования
# наследование проверяет методы у предков в порядке их указания в описании наследования
# если у предков есть общий предок то проверябтся все предки до общего предка и только подом обший предок


# MixIn - по сути примесь
# это маленькие классы которые имеют небольшой набор функций и подмешиваются к другим классам становясь родителями
# целевого класса, идея миксинов предполагает их импользование только вместе с другими классами для кастомизации или
# расширения функционала дочерних классов. Создание экземпляров у мискинов не предполагается


class MixinFood:  # миксин. просто класс, который позволяет обеспечить другой класс какой либо дополнительной
    # функциональностью, или когда есть необходимость добавить одну и ту же функциональность нескольким классам
    # не связанными между собой родственными связями
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print(f'I like {self.food}')


class Person:
    def hello(self):
        print('I am Person')


class Student(MixinFood, Person):
    food = 'Pizza'

    def hello(self):
        print('I am Student')


s = Student()
s.get_food()