#!/usr/bin/env python
#coding: UTF-8

import csv
with open('csv_test.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerow([1,'スパム','500円'])
    writer.writerow([2,'卵','168円'])
    writer.writerow([3,'ベーコン','1,250円'])

# ファイル読み込みモードについて
# 'r' 読み込み用に開く (デフォルト)
# 'w' 書き込み用に開き、まずファイルを切り詰める
# 'x' 排他的な生成に開き、ファイルが存在する場合は失敗する
# 'a' 書き込み用に開き、ファイルが存在する場合は末尾に追記する

# 'b' バイナリモード
# 't' テキストモード (デフォルト)
# '+' ディスクファイルを更新用に開く (読み込み／書き込み)

# ‘tr’ などとして、上記文字を組み合わせる事も可能
	
# ※注意点としてWindows環境を使用しているとデフォルトがcp932でコーディングされる。
# ⇒対策 encoding="utf-8" を引数として加える。e.g. f = open('test.json', 'r', encoding="utf-8")
# encoding="utf-8_sig" の時もあるとか


# 読み込み
with open('csv_test.csv', 'r', encoding='utf-8') as f:
	reader = csv.reader(f)
	
