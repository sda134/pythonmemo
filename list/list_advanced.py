#!/usr/bin/env python
#coding: UTF-8

# 同じ値の要素を複数作成する
list_of_all_two = [2 for i in range(5)]    # これは itertools の repeat() でも同じ事ができる


# それぞれに同じような加工を施す
add7 = lambda n: n + 7
sharp_list = [28, 31, 27, 30, 26, 29, 25 ]
new_list = [add7(i) for i in sharp_list]   # この [] は必要。ないと実行エラー。

# 条件付きリストの作成　python の三項演算子
# なお、elseなしでも問題はない
odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]

# 一方は変数、一方はlist として宣言する
a1, *b2 = 100, 200, 300     # 左辺、右辺の数があっていない時は
*a2, b2 = 100, 200, 300     # *がある変数に list として代入される  *が無ければエラーとなる


# ２項以上の変数同時代入を応用した方法
pref = ["静岡県", "愛知県", "三重県", "岐阜県"]
capital = ["静岡市", "名古屋市", "津市", "岐阜市", "奈良市"]
designated = [["静岡市", "浜松市"], ["名古屋市"], []]

for p, c, d in zip(pref, capital, designated):
    dstr = "なし"
    if(len(d) > 0):
        dstr = ", ".join(d)
    print("{0} の県庁所在地は {1} 政令指定都市は {2}".format(p, c, dstr))

print('- ' * 10 + '\n')
    

# リストの要素すべてに処理
print('even only:%s\n' %\
    [i for i in range(-10,10) if i % 2 == 0])   # 条件付きで新しいリストを作成 　※[]で閉じる必要がある　[ 処理 for arg in list]
print('all exponential:%s\n' %\
    [i**2 for i in range(-10,10)])  # 処理を施した新しいリストの作成
    

# Generics
from typing import (TypeVar, Sequence)
T = TypeVar('T')  # Can be anything
def repeat(x: T, n: int) -> Sequence[T]:
    return [x]*n

print(repeat(str,3))
print('- ' * 10 + '\n')


# filter & assert
def is_even(x):
    print("in is_even({x})".format(x=x))
    return x % 2 == 0

# 意味不明 21-01-23
#gen_exp = (x for x in range(10) if(is_even(x)))
#assert type(gen_exp) == GeneratorType
#assert (next(gen_exp), next(gen_exp), next(gen_exp)) == (0, 2, 4)

filterd = filter(is_even, range(10))
print(filterd)
