from analyzetest.replaceanalyze import *
import cProfile

cProfile.run("slowest_replace('test str')")
# cProfile.run("timeit_profile()", "timeit")
# p = pstats.Stats('timeit')
# p.sort_stats('time')
# p.print_stats(6)
