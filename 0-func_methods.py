class Person:
    name = 'Ivan'

    def hello(self, qqq='xxx'):
        print('hello', qqq)


a = Person()
b = Person()

for i in [Person, a, b]:
    print('id', hex(id(i)))
    print('id .hello', hex(id(i.hello(i))))
    print('type .hello', type(i.hello))
    print('id .name', hex(id(i.name)))
    print('+-+-+-+-+-+-+')
