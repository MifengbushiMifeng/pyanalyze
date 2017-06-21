class StaticClass():
    value = 12
    item = ''

    @staticmethod
    def _plus(a, b):
        return a + b

    def __init__(self, value):
        self.value = self._plus(value, value)


def func():
    a = StaticClass()
    a.item = 'TOY'
    a.value = 121212
    b = StaticClass()
    print(a.item + ' / ' + str(a.value))
    print(b.item + ' / ' + str(b.value))


if __name__ == '__main__':
    func()
