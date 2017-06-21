def func(flag=False):
    if flag:
        print('The func will run.')
    else:
        print('The func will not actually run.')


if __name__ == '__main__':
    func()
    func(True)
    a_str = ''
    print(a_str.replace('-', '??'))
    a_str = 'a-b'
    print(a_str.replace('-', '??'))
    a_str = ''
    if a_str:
        print(' a_str ')
    a_str = '1234'
    if a_str is not '123':
        print('This is not 123')
