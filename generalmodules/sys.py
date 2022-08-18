#!/usr/bin/env python3
#coding: UTF-8


import os
import sys  # システムパラメータと関数を扱う https://docs.python.org/ja/2.7/library/sys.html



# path ：
print(sys.path[0])                  # path[0] は自身のディレクトリを返す
print(os.path.dirname(__file__))    # その為，この２つは同じ結果になる
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # 親ディレクトリをモジュール読み込みの対象に加える


print('sys.path\n%s\n' % sys.path)            # ライブラリ検索の対象となるディレクトリのリストを返す
print('sys.copyright\n%s\n' % sys.copyright)  # インタプリタの著作権を表示する


