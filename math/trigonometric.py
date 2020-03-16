#!/usr/bin/env python
#coding: UTF-8

import math



# ラジアン
print(f'degrees from radian：\t{math.degrees(math.pi):.2f}')
print(f'radian from degrees：\t{math.radians(180):.5f}')

# 三角関数
print(f'sin30：\t\t\t{math.sin(math.radians(30)):.5f}')
print(f'radian of arctangent30：{math.atan(30):.5f}')
print(f'degree of arcsine(0.5)：{math.degrees(math.asin(0.5)):.2f}')


# 終了
ret =input('何かキーを押してください')