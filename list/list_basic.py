#!/usr/bin/env python
#coding: UTF-8

# list ,tuple, dict, range 集合の違い
list_eg = ["A", "B", "C", "D", "E"]            # []で閉じる mutable(後で内容を変更可能)
tuple_eg = ('A','B','C','D','E')               # ()で閉じる immutable(書き換え不能)　詳細は Tuple.pyへ
range_eg = list(range(0,10,3))                 # sequence 型（forを用いた関数の様なもの）を生成。特殊なパターンを扱う
dict_eg = {'USA': 1, 'JAPAN': 2, 'Germany': 3} # {}で閉じる key は一意でないといけない　詳細は Dict.pyへ
set_eg = set(["USA","JAPAN","Germany","JAPAN"])

# 各変換
tuple_from_list = tuple(list_eg)
list_from_tuple = list(tuple_eg)
list_from_dict_key = dict_eg.keys()
list_from_dict_val = dict_eg.values()
tuple_from_dict = tuple(dict_eg.items())


# 基本中の基本
items = [1,2]

b_ret = 2 in items      # C# の List.exists() に近い使い方

items.append(3)         # append ｃ＃などの.Add()
items.insert(1, 1.5)    #(index, value) indexは0 から始まる
items.extend([3,4])     # リストをまるごと追加 C#の .AddRange() のようなもの

print("length of list: %i" % len(items)) #　※注意！ list.count メソッドもあるが、意味が違う(出現回数)

p = items.pop()      # 最後、もしくは指定index の要素を削除しつつ取得(pop) する
print("items.pop(): %i" % p)

cp = items.copy()   # shallow copy であることに注意！
cp.reverse()
items.extend(cp)    # リストをまるごと追加 C#の .AddRange() のようなもの

print ('index:' + str(items.index(1))) # 一致した値の、一番最初のindex 番号を返す
items.remove(1)        #  一致した値の、一番最初の item を削除

for h in items:     
    print(h)


# 関連する組み込み関数 :https://docs.python.org/ja/3/library/functions.html
byteArr = bytearray([0x01,0x02]) # バイト配列　※詳しくは /data/bytes を参照
items_rev = list(reversed(items))
items_sort_rev = sorted(items, reverse = True)
items_0to5 = range(5)

test = 1

