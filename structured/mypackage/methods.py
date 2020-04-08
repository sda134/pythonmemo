#!/usr/bin/env python
#coding: UTF-8

from class_samples import TestClass as csmp   # 自作モジュールの import (同じフォルダにある場合)
# from Children.Class import TestClass    # 一つ下のフォルダにある場合 

'''
・ファイル名をクラス名と重複させる事も可能 例）from TestClass import TestClass
・呼び出し元のファイルにエラーがあると import できない　
'''


with csmp() as ts:
    ts.PublicPrint('hoge')

# 引数の型指定　※但しこれは使う人への情報以上の意味は無い
def Greeting(arg :str) -> str:
    '''
    saying hello\n
    doc string マウスでホバーさせた時や，__doc__で表示できる。
    '''
    return "Hello! :%s" % arg
print('Greeting.__doc__:%s' % Greeting.__doc__)                 #
print('Greeting.__annotations__:%s' % Greeting.__annotations__) # 
print('Greeting.__module__:%s' % Greeting.__module__)           # class method なら class 名。それ以外の間合いは __main__ が返る
print('-' * 30 + '\n')


def DefaultArg(arg='hoge'):
    print("Method:DefaulutArg %s" % arg)

def JoinedStr(*arg):     # JoinedStr("1","2","3") の様に呼び出す 慣例的に *arg だとか **kwargs が使われる
    print(','.join(arg)) # **arg だとdic 型になる。呼び出し側でも変数を使う時は同じ


# dic 引数の渡し方とunpack
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)



# python3 限定だが、 '*' 以降はキーワード専用引数となり、オプショナル引数を明示できる
def do_some_great_stuff(arg_a, arg_b, *, logger=None):
    pass

DefaultArg()


# help(TestClass)

# Python の引数はすべて ref（参照渡し
# 参照渡しの検証
def AddOneItem(arg):
    arg.append('hoge')

items = ['fuga']  # この時点での len(items) は 1
AddOneItem(items)
print(len(items)) # 結果: 2 と表示


# 但し値渡しの様な振る舞いをするものもある。→ Immutable
'''
•Immutable な型  int, float, str, tuple, bytes, frozenset 等
•Mutable な型    list, dict, set, bytearray 等
'''
# immutable の検証
def AddOne(arg):
    arg += 1


iVal = 1
AddOne(iVal)
print(iVal) # 結果：1 と表示

