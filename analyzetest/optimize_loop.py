#!/usr/bin/env python
# -*- coding: utf-8 -*-
from timeit import Timer

lowerlist = ['this', 'is', 'lowercase']
exec_times = 100000


def to_upper1():
    upper = str.upper
    uppserlist = []
    append = uppserlist.append
    for word in lowerlist:
        append(upper(word))
    # print(uppserlist)
    return uppserlist


def to_upper2():
    uppserlist = []
    for word in lowerlist:
        uppserlist.append(word.upper())
    return uppserlist


# def _timeit_analyze_(func):
#     t1 = Timer("%s('%s')" % (func.__name__, orignal_str), 'from __main__ import %s' % func.__name__)
#     print('{:<20}{:10.6} s'.format(func.__name__ + ':', t1.timeit(exec_times)))

def _timeit_analyze_(func):
    t = Timer('%s()' % func.__name__, 'from __main__ import %s' % func.__name__)
    print('{:<20}{:10.6} s'.format(func.__name__ + ':', t.timeit(exec_times)))


_timeit_analyze_(to_upper1)
_timeit_analyze_(to_upper2)
