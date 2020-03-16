#!/usr/bin/env python
#coding: UTF-8

# map: listの各要素に同じ操作をする 
def add1(str):          # ’1’を追記する関数      
      return str+'1'
addedList = map(add1, ['a', 'b', 'c'])
for s in addedList:
    print(s)

 # filter 条件に合うものを抽出
list_words = ['toy', 'cat', 'dog', 'girl', 'house', 'boy']
result = filter(lambda x : len(x)==3, list_words)
for item in result:
    print(item)

# enumerate 自動で連番を振る
result = list(enumerate(['Spring', 'Summer', 'Fall', 'Winter']))
for item in result:
    print(item)

# range : listの自動作成　※これを generator 式と呼ぶ
list_0_to_9 = list(range(10))
list_1_to_8 = list(range(1,9))
list_step_by_5 = list(range(0,30,5))
for item in list_step_by_5:
    print(item)

# index     要素番号を返す  ※但し、存在しない要素を指定するとエラー
for item in list_step_by_5:
    idx = list_step_by_5.index(item)
    print("item: %s, idx: %i" % (item, idx))

# enumerate  上のindex とほぼ同じ
for idx, item in enumerate(list_step_by_5):
    print("item: %s, idx: %i" % (item, idx))

# yield
def MoreThan2():
    for iVal in range(5):
        if iVal > 2:
              yield iVal



hoge =MoreThan2()
repr(hoge)

# del 文    リストから要素を削除
print('削除まえ %s' % repr(list_words))
del list_words[0]
print('削除まえ %s' % repr(list_words))
# del hoge[0]    # generator で作ったリストは削除できないらしい




import itertools    # itertools C#のlinq っぽく、listの加工メソッドの集まり


test= 1
