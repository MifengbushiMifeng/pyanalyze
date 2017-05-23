#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cProfile
import re
import pstats
import os
import functools


# cProfile.run('re.compile("foo|bar")')

def do_cprofile(filename):
    """
    decorator for function profiling
    :param filename: 
    :return: 
    """

    def wrapper(func):
        @functools.wraps(func)
        def profiled_func(*args, **kwargs):
            # Flag for do profiling or not.
            # DO_PROF = os.getenv('PROFILING')
            DO_PROF = True
            if DO_PROF:
                profile = cProfile.Profile()
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                # Sort stat by internal time.
                sortby = 'tottime'
                ps = pstats.Stats(profile).sort_stats(sortby)
                ps.dump_stats(filename)
            else:
                result = func(*args, **kwargs)
            return result

        return profiled_func

    return wrapper


# print(f(5))


# A sample of catch the return result
class Memoized(object):
    def __init__(self, func):
        self.func = func
        self.results = {}

    def __get__(self, instance, cls):
        self.instance = instance
        return self

    def __call__(self, *args):
        key = args
        try:
            return self.results[key]
        except KeyError:
            self.results[key] = self.func(self.instance, *args)
            return self.results[key]


# @do_cprofile('./f.prof')
@Memoized
def f(self, n):
    if n < 2:
        return n
    return f(n - 2) + f(n - 1)


f(5)
f(5)
