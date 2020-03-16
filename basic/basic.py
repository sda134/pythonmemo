#!/usr/bin/env python
#coding: UTF-8


# コード改行    \ を使う
return_of_long_line = 1 + 2 + 3 + \
    4 + 5

# 複数の変数への代入
a,b,c = 100, 200,'hoge'
e,*f = 100, 200,'hoge'


# コマンドライン引数
import sys
args = sys.argv          # 引数の一つ目 arg[0] は python 実行時の第一引数、つまり本ファイルのパスになるらしい

if __name__ == "__main__":                      # 外から呼び出された場合、 __name__ は　'__main__' になる
    print('executed from outside!')
    print('length of args: %s' % len(args))
    for a in args:
        print('item: %s' % a)

# private 変数 __name__ 
# 通常 module 名、class 名などが代入される。def.='__main__'
print('__name__:%s' % __name__)


# 終了
ret =input('何かキーを押してください')

