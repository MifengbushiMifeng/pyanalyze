import threading

import time


class MyThread(threading.Thread):
    def run(self):
        while True:
            time.sleep(5)
            print('calling as a thread')


def call_thread():
    a_thread = MyThread()
    a_thread.start()


def call_not_thread():
    while True:
        time.sleep(5)
        print('calling NOT as a thread')


if __name__ == '__main__':
    print('process start to run')
    # call_not_thread()
    call_thread()
    time.sleep(3)
    print('process end without block')
