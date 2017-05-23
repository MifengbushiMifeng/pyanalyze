from analyzetest.replaceanalyze import *
import cProfile
import re

cProfile.run("slowest_replace('test str')")


# cProfile.run("timeit_profile()", "timeit")
# p = pstats.Stats('timeit')
# p.sort_stats('time')
# p.print_stats(6)


def fibonacci(i):
    if i < 2:
        return i
    return fibonacci(i - 2) + fibonacci(i - 1)


print(fibonacci(1))

cProfile.run('re.compile("foolbar")')


# http://python.jobbole.com/85381/
# http://python.jobbole.com/87621/?utm_source=blog.jobbole.com&utm_medium=relatedPosts
