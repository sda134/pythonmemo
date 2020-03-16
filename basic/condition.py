#!/usr/bin/env python
#coding: UTF-8

num =int(input('数値を入力してください'))

# 条件分岐：基礎
if num > 100:
    print('more than 100')    
elif num == 50:                  # C#などと同じく等価は ==
    print('the value is 50')    
elif num > 50:
    print('more than 50, less than 100')
else:
    pass


if num != 0:        # !=　はpython でも普通に使える 
    print('not zero')
if not num == 1:    # どちらを使っても良いらしい
    print('not 1 either')

if not num >= 20:  # C系の ! を使うような感じ
    print('less than 20')


# こんな書き方もできる
a =2
b = 4
if 3>a>1<b<5: print(a, b)
if (0<b)*(a>0): print(a, b)  # この場合 * は≒and 短絡評価になるが


# 複数行の条件
if (num > 0 and              # () の使用
    num < 20):
    print('positive value and less than 20')

if num > 50 \
    or num % 2 == 0:          # バックスラッシュの使用 ※但し / の後に# が使えない上、読みにくい
    print('even number or more than 50')


# python に switch はないので、if と elif で書く
s = 'a'
if s == 'a' or s == 'b':
    print('a or b')
elif s == 'c':
    print('c')

# 三項演算子
x = "more than 50" if num > 50 else "less than/equal 50"
print(x)