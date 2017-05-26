#!/usr/bin/env python
# -*- coding: utf-8 -*-
num = [1, 4, -5, 10, -7, 2, 3, -1]
new_list = [x ** 2 for x in num if x > 0]
new_gen = (x ** 2 for x in num if x > 0)

print(new_list)
print(new_gen)

for item in new_gen:
    print(item)

n = 16
myDict = {}
for i in range(0, n):
    char = 'abcd'[i%4]
    if char not in myDict:
        myDict[char] = 0
        myDict[char] += 1
        print(myDict)