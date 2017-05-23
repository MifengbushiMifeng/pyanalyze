#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pstats

p = pstats.Stats('f.prof')
p.strip_dirs().sort_stats('cumtime').print_stats(10, 1.0, '.*')
