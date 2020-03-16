#!/usr/bin/env python
#coding: UTF-8

# ラムダ式　基本
lambda_test = lambda n: n * 2
lambda_no_arg = lambda: print('***no arg***')
lambda_2args = lambda x,y : x * y
lambda_multi_rows = lambda : [
    print('hoge'),
    print('fuga')
    ]

# 基本ラムダ式の実行
print('test:\t%s' % lambda_test(1))
print('no arg:\t%s' % lambda_no_arg())      # ラムダの実行が先。戻り値は後。
print('2args:\t%s' % lambda_2args(3,4))
lambda_multi_rows()


# python.org turorial より
print('= ' * 10 + 'from python.org turorial' + ' =' * 10)
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(repr(pairs))          # 結果：[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

def make_incrementor(n):    # ラムダ式を返す関数。これにより、入れ子の関数が作成できる。
    return lambda x: x + n
f = make_incrementor(42)    # 42 を足す関数を動的に作成した感じ
print(f(1))                 # 結果：43 
