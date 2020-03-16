#!/usr/bin/env python
#coding: UTF-8

# https://docs.python.org/ja/3/library/configparser.html

import configparser
 
ini = configparser.ConfigParser()
ini.read('./dat/config.ini', 'UTF-8') # iniファイル読み込み ≒open?

print(ini['DEFAULT']['debug'])     # こちらのアクセス方法が推奨されている　セクション名, パラメータ名
print(ini.get('DEFAULT', 'debug')) # get メソッドでも同じ結果になる


count_i = 0

try:                               # パラーメータ名が存在しないとエラーになるらしい
    count = ini['DEFAULT']['reboot']
except Exception as e:
    print('exception! %s' % e)
else:
    count_i = int(count)
    count_i += 1
finally:
    ini['DEFAULT']['reboot'] = str(count_i)

# 上までの処理ではファイルは変更されていない
with open('./dat/config.ini', 'w') as f:
    ini.write(f)