#!/usr/bin/env python
#coding: UTF-8

import math

def traversePointList():
    # パラメータSET

    bandWidth =float(input('バンド幅？')) # 線径の入力
    bandMove =float(input('バンド移動量？')) # 線径の入力
    bandTimes =int(input('バンド回数？')) # 線径の入力
    for b in range(bandTimes + 1):
        clac_w = bandWidth * b
        clac_m = bandMove * b
        print('トラバース位置 %i\t幅：%f\t移動：%f' % ((b+1), clac_w, clac_m))


traversePointList()
# 終了
ret =input('何かキーを押してください')