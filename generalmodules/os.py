#!/usr/bin/env python3
#coding: UTF-8


import os

# path ：https://docs.python.org/ja/2.7/library/os.path.html
print('__file__:\t%s' % __file__)
print('abspath:\t%s' % os.path.abspath(__file__))           # abspath：絶対path を返す __file__ と何が違う？
print('dirname:\t%s' % os.path.dirname(__file__))           # dirname：ファイル名を省いたディレクトリ名を返す
print('path.join:\t%s' % os.path.join('C\\:', 'usr', 'src'))  # join  ：path の文字列を少し楽に作れる

