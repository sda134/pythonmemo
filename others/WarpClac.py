#!/usr/bin/env python
#coding: UTF-8

import math

def clac_traversePitch():
    # パラメータSET
    bandCount = 40

    wireDiameter =float(input('線径？')) # 線径の入力

    # 計算
    area = wireDiameter **2 * math.pi / 4 # ボビン面積
    volume = 470 / 8                      # 体積 ※8 ≒ sus304 の比重7.93；470 ボビン重量
    length = volume /area                 # ボビン長さ

    # 森石さんの計算
    clac = 470 /(((wireDiameter/2) **2) * math.pi * 8) 
    print('森石さん計算 %f' % clac)

    print('ボビン長さ %f' % length)
    print('整経長さ %f' % (length /bandCount))

def clac_beamRevCount():
    # パラメータ設定部
    beamLength = 50       # ビーム長さ[m]
    beamLength *= 1000    # ビーム長さ[m → mm]
    wireDiameter = 1    # 線径
    beamDiameter = 295
   
    revolutionCount =0      # ビーム回転数を示すループカウンタ

    while beamLength > 0:
        beamLength -= (beamDiameter * math.pi) # 周長分減算
        beamDiameter += (wireDiameter * 2)     # 線径一巻き分直径を加算する
        revolutionCount +=1

    print('ビーム回転回数: %i' % revolutionCount)
    print('ビーム直径　　: %f' % beamDiameter)
    print('A相パルス数　 : %f' % (1000.0 * 100.0 / (beamDiameter * math.pi)))

clac_beamRevCount()
clac_traversePitch()

# 終了
ret =input('何かキーを押してください')