class AClass(object):
    def __init__(self, dep):
        self._dep = dep
        self._name = 'Tester'
        self._age = '20'

    def set_info(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return self._name + ' / ' + str(self._age) + ' / ' + self._dep


if __name__ == '__main__':
    a_class = AClass('DEV')
    info = a_class.get_info()
    print(info)
    a_class.set_info('Jon', 27)
    info = a_class.get_info()
    print(info)

    b_class = AClass('TEST')
    info_b = b_class.get_info()
    print(info_b)
