#!/usr/bin/env python
# -*- coding: utf-8 -*-
from timeit import Timer


def slowest_replace(orignal_str):
    replace_list = []
    for i, char in enumerate(orignal_str):
        c = char if char != ' ' else '-'
        replace_list.append(c)
    return ''.join(replace_list)


def slow_replace(orignal_str):
    replace_str = ''
    for i, char in enumerate(orignal_str):
        c = char if char != ' ' else '-'
        replace_str += c
    return replace_str


def fast_replace(orignal_str):
    return '-'.join(orignal_str.split())


def faster_replace(orignal_str):
    return orignal_str.replace(' ', '-')


# def _time_analyze(func, orignal_str, exec_times):
#     from time import clock
#     start = clock()
#     for i in range(exec_times):
#         func(orignal_str)
#     finish = clock()
#     print('{:<20}{:10.6} s'.format(func.__name__ + ":", finish - start))


exec_times = 100000
orignal_str = 'I would like to test the replace func.'


# _time_analyze(slowest_replace, orignal_str, exec_times)
# _time_analyze(slow_replace, orignal_str, exec_times)
# _time_analyze(fast_replace, orignal_str, exec_times)
# _time_analyze(faster_replace, orignal_str, exec_times)
def _timeit_analyze_(func):
    t1 = Timer("%s('%s')" % (func.__name__, orignal_str), 'from __main__ import %s' % func.__name__)
    print('{:<20}{:10.6} s'.format(func.__name__ + ':', t1.timeit(exec_times)))


_timeit_analyze_(slowest_replace)
_timeit_analyze_(slow_replace)
_timeit_analyze_(fast_replace)
_timeit_analyze_(faster_replace)
