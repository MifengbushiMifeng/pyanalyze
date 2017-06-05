#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_file():
    with open(r"C:\Jonzhou\test", 'w', encoding='utf-8') as f:
        f.write('name: 1' + 'Jonathan' + '\n')
        f.write('age: ' + 27 + '\n')


if __name__ == '__main__':
    create_file()
