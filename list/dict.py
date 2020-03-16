#!/usr/bin/env python
#coding: UTF-8

# https://docs.python.org/ja/3/library/stdtypes.html?highlight=dict#dicts

# dict 型の基本　※注目すべきは型の異なるメンバを含む事ができる点
myDict = {'key1': 10, 'key2': 'foo'}
myDict['key3'] = 'o1'                # キーを追加（通常は値を代入）
print(myDict['key3'])                # キー　で値にアクセスする


if('key4' not in myDict):            # key in dict / key not in dict
    print('key4 does exist.')

for dictKey in myDict.keys():
    print(dictKey)

for dictVal in myDict:         # これも myDict.keys と同じ結果になる
    print(dictVal)

for dictVal in myDict.items(): # dict の要素にしたい場合は items()
    print(dictVal)

for dictVal in myDict.values(): # 値
    print(dictVal)



# 値が複数個数の dictの 作成
# ※基本的には出来ないと思った方が良い。groupby の結果などが値を複数もつ dictとなる
words = ['apple', 'orange', 'banana', 'alpha', 'beta']
results = {}                                            # 空のdict を生成
for word in words:
    results.setdefault(word[0], []).append(word)

# 注意点
sortedDic = sorted(myDict) # sorted を使用すると list になる
print(type(sortedDic))     # 結果:<class 'list'>

# dict に似た型で、set と言うものがある
mySet = {'set1','set1','set1'}
print(type(mySet))