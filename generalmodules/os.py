#!/usr/bin/env python3
#coding: UTF-8


import os

# パス関連
# path ：https://docs.python.org/3/library/os.path.html
print('__file__:\t%s' % __file__)
print('environ:\t%s' % os.environ['HOME'])                      # 環境変数を使用 environ.get("home") でも良い
print('abspath:\t%s' % os.path.abspath(__file__))               # abspath：絶対path を返す __file__ と何が違う？
print('upperdir:\t%s' % os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print('dirname:\t%s' % os.path.dirname(__file__))               # dirname：ファイル名を省いたディレクトリ名を返す
print('path.join:\t%s' % os.path.join('C\\:', 'usr', 'src'))    # join  ：path の文字列を少し楽に作れる

for dir, subdir, files in os.walk(os.path.dirname(__file__)):   # walk : 特定ディレクトリ内のディレクトリやファイルを返す
    print(dir)

# 対象ディレクトリがなければ作成する例
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
