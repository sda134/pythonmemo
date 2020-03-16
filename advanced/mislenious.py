#!/usr/bin/env python
#coding: UTF-8

# あまり使わないかもしれない雑多情報のメモとする

# type を使って Class を動的に定義する
def function1(self, args):
    pass

ClassName = type('ClassName',
                 [1,2,],
                 {'attribute1': 3,
                  'function1': function1,})
cs = ClassName()