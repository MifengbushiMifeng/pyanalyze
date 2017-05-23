#!/usr/bin/env python
# -*- coding: utf-8 -*-
num = [1, 4, -5, 10, -7, 2, 3, -1]
new_list = [x ** 2 for x in num if x > 0]
new_gen = (x ** 2 for x in num if x > 0)

print(new_list)
print(new_gen)

for item in new_gen:
    print(item)
