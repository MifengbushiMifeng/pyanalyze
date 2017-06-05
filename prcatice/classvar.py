class AClass(object):
    class_value = 'test123'

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = AClass('a')
    b = AClass('b')
    print(a.name, '/', a.class_value)
    print(b.name, '/', b.class_value)
    a.class_value = 'testa'
    print(a.name, '/', a.class_value)
    print(b.name, '/', b.class_value)
    b.class_value = 'testb'
    print(a.name, '/', a.class_value)
    print(b.name, '/', b.class_value)

    print('-----------------------------')
    print(AClass.class_value)
