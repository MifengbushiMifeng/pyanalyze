class Person(object):
    name = 'new user'
    age = 0
    email = ' '
    address = ' '

    # def fun2(self):
    #     Person.__fun()

    def __fun(self):
        print('__fun 1')

    def __fun(self, name):
        print('__fun2')


def set_information(person: Person):
    person.name = 'Jonathan'
    person.age = 25
    person.email = 'test@12345.com'
    person.address = 'Dalian China'


def create():
    ins = Person()
    print(ins.name)
    set_information(ins)
    print(ins.name)
    print(ins.age)
    print(ins.email)
    print(ins.address)


if __name__ == '__main__':
    create()
