#!/usr/bin/env python
#coding: UTF-8

import os



# 定義済変数
print("__file__ %s" % __file__)

# パス関連
print(os.path.dirname(os.path.dirname(__file__))) # フォルダまでのパスを返す（入れ子で使える）

