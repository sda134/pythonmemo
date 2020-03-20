#!/usr/bin/env python
#coding: UTF-8

# 同じ値の要素を複数作成する
list_of_all_two = [2 for i in range(5)]    # これは itertools の repeat() でも同じ事ができる


# それぞれに同じような加工を施す
add7 = lambda n: n + 7
sharp_list = [28, 31, 27, 30, 26, 29, 25 ]
new_list = [add7(i) for i in sharp_list]   # この [] は必要。ないと実行エラー。

# 条件付きリストの作成（同じような加工…の更に応用）
odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]

# 一方は変数、一方はlist として宣言する
a1, *b2 = 100, 200, 300     # 左辺、右辺の数があっていない時は
*a2, b2 = 100, 200, 300     # *がある変数に list として代入される  *が無ければエラーとなる


from typing import (TypeVar, Sequence)

# Generics
T = TypeVar('T')  # Can be anything
def repeat(x: T, n: int) -> Sequence[T]:
    return [x]*n

print(repeat(str,3))
print('hoge')
