def func(input_str: str):
    while 1:
        if len(input_str) > 10:
            input_str = input_str[1:]
        else:
            break
    print(input_str)


if __name__ == '__main__':
    func('123456789')
    func('1234567890-0987654321')
