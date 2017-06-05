#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time


def doWaiting():
    print('thread doWaiting is running')
    print('start waiting', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))
    print('thread doWaiting is stopped!')


def runThread():
    print('main process is running')
    thread1 = threading.Thread(target=doWaiting)
    thread1.start()
    print('start join')
    print('----------')
    print('----------')
    print('----------')
    print('----------')
    thread1.join()
    print('end join')
    print('main process is stopped!')


if __name__ == '__main__':
    runThread()
