#!/usr/bin/env python
#coding: UTF-8

import glob
import os
import shutil
from distutils.dir_util import copy_tree


# current_directory = os.path.dirname(__file__)   # 現在のフォルダパス　※これはpackage を作る時によく使う

print('dirname of __file__:\t\t%s' % os.path.dirname(__file__))
print('basename of __file__:\t\t%s' % basename =  os.path.basename(__file__))
print('current work directory[cwd]:%s' % os.path.dirname(os.getcwd()))

# ファイル名のリストを取得
file_list =glob.glob("./*")
os.listdir(./)                  # os を使った方法

for fn in file_list:
    path, ext = os.path.splitext(fn) # 拡張子とファイル名に分離
    alterd_fn = fn
    # os.rename(alterd_fn, path + ".csv")
    
    print('full: %s' % fn)
    print('path: %s' % path)
    print('ext: %s' % ext)


# ディレクトリ有無を確認して、なければ作成
if not os.path.exists("./copied"):
    os.mkdir("./copied")

# ファイルコピー
shutil.copy('./files.py', './copied/files_copied.py')

# ディレクトリごとコピー
copy_tree('./copied','./copied_duplicated')

# ディレクトリ削除
os.rmdir('./copied')        # 中身が空でないと削除できない
shutil.rmtree(target_dir)   # 中のファイル、ディレクトリを削除
