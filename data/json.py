#!/usr/bin/env python
#coding: UTF-8

import json


# json ファイルの読み込み
f = open('./dat/devices.json', 'r', encoding="utf-8")
jsonData = json.load(f) # 読み込んでdict 型に変換
f.close()

# json → list   ※ property set が記述してあると、自動で格納してくれる
deviceList = [ dev for dev in jsonData]
test = 1