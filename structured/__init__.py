#!/usr/bin/env python
#coding: UTF-8

# このファイルを作っておくと、 import フォルダ名で一括で importできる。
# つまり、module 化される。
# 
# (python3からは、module化する際に __init__.pyファイルは必須ではなくなった)

from . import class_samples             # . で自身のファイルと同じディレクトリにあるファイルに
from . import enum_samples              # .. で親パッケージ？（ディレクトリだと思うが）を相対的に参照できる

__all__ = ['say_hi', 'say_hello']       # from my_package import * でimport される時の対象メンバ。 
                                        # 但し、import * は非推奨なので、書く機会は少ないと思われる

def say_hi():
    print('hi!')

def say_hello():
    print('hello!')

def say_bye():
    print('bye!')
