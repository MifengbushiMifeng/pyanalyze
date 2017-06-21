class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_person_info(self):
        return self._name + ' / ' + str(self._age)


def func(some_one: Person):
    str = some_one.get_person_info()
    print(str)


if __name__ == '__main__':
    p = Person('Jonathan', 27)
    func(p)
