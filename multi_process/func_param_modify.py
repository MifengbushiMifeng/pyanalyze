def modify_param(param):
    param = param + '/' + 'param has been changed!'
    print('modify_param :' + param)


def call_modify_param():
    param = 'param initial'
    modify_param(param)
    print('call_modify_param:' + param)


if __name__ == '__main__':
    call_modify_param()
