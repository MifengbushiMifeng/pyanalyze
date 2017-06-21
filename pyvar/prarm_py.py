def func(param: str):
    if param.endswith("string"):
        print('The parameter is string')
    else:
        print('The parameter is NOT string')


class MyClass(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return self._name + ' / ' + str(self._age)


def func_my_class(param: MyClass):
    info = param.get_info()
    print(info)


if __name__ == '__main__':
    func('I am string')
    my_class = MyClass('Jonathan', 27)
    func_my_class(my_class)
