#!/usr/bin/env python
#coding: UTF-8

# 特徴
# range はシーケンス型と呼ばれ、特殊なパターンを扱う
# immutable (変化できない)

# 基本
print("list(range(0,10,3)):\t%s" % list(range(0,10,3)))     #
print("list(range(10)):\t%s\n" % list(range(10)))           # ※10が出力され無い事に注目
print('list(reversed(range(3, 10, 2))):\t%s' % list(reversed(range(3, 10, 2))))
print('compare: list(range(10, 3, -2)):\t%s\n' % list(range(10, 3, -2)))


# for で用いる
for i in range(3):
    print(i)

for i in reversed(range(3)):
    print(i)


