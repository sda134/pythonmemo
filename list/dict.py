#!/usr/bin/env python
#coding: UTF-8

# https://docs.python.org/ja/3/library/stdtypes.html?highlight=dict#dicts

# dict 型の基本　※注目すべきは型の異なるメンバを含む事ができる点
my_dict = {'key1': 10, 'key2': 'foo'}
my_dict['key3'] = 'o1'                # キーを追加（通常は値を代入）
print(my_dict['key3'])                # キー　で値にアクセスする

other_dict = {'key1': 4.0, 'key4': 4.0} # 
my_dict.update(other_dict)              # update 複合的なdict の更新
print('\n' + '-' * 30)


if('key5' not in my_dict):            # key in dict / key not in dict
    print('key5 does exist.')
print('\n' + '-' * 30)

print('keys()')
for dictKey in my_dict.keys():
    print(dictKey)
print('\n' + '-' * 30)

print('my_dict')
for dictVal in my_dict:         # これも my_dict.keys と同じ結果になる
    print(dictVal)
print('\n' + '-' * 30)

print('values()')
for dictVal in my_dict.items(): # dict の要素にしたい場合は items()
    print(dictVal)
print('\n' + '-' * 30)

print('values()')
for dictVal in my_dict.values(): # 値
    print(dictVal)
print('\n' + '-' * 30)



# 値が複数個数の dictの 作成
# ※基本的には出来ないと思った方が良い。groupby の結果などが値を複数もつ dictとなる
words = ['apple', 'orange', 'banana', 'alpha', 'beta']
results = {}                                            # 空のdict を生成
for word in words:
    results.setdefault(word[0], []).append(word)

# 注意点
sortedDic = sorted(my_dict) # sorted を使用すると list になる
print(type(sortedDic))     # 結果:<class 'list'>

# dict に似た型で、set と言うものがある
mySet = {'set1','set1','set1'}
print(type(mySet))