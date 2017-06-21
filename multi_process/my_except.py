def base_exception():
    print('base_exception start')
    middle_func()
    print('base_exception finish')


def middle_func():
    try:
        raise_exception()
    except:
        print('An exception occurred!')


def raise_exception():
    raise IOError;


if __name__ == '__main__':
    base_exception()
