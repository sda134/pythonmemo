#!/usr/bin/env python
#coding: UTF-8

import math

arg = 5/3
print(arg)

a = 1
a += 1                      # += の表現も普通に使える
print('a : {}'.format(a))

print('5/3 : %i' % (5/3))                    # 除算
print('5//3 : %i' % (5//3))                  # 切り下げ除算

print('1.5 ** 2 : {0}'.format(1.5 ** 2))     # 累乗
print('√ 3 : %f' % math.sqrt(3))             # 平方根
print('√ 3 : %f' % round(math.sqrt(3), 4))   # 丸め

print(f'pi：{math.pi:.5f}')                 # 表示桁数　＋α math.pi（円周率）はプロパティ（メソッドでは無い）

sin30 = math.sin(math.radians(30))          # 三角関数（詳しくは trigonometric.py を参照)
print(math.isclose(sin30, 0.5))             # 誤差を考慮して比較

# 終了
ret =input('何かキーを押してください')