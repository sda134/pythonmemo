#!/usr/bin/env python
#coding: UTF-8

# 参考資料：https://docs.python.org/ja/3/library/functions.html
# 時間の許す限り試していく
import math

print('abs　絶対値'+ ' -' *10)
print(f'abs(-1):\t{abs(-1)}\n')

print('all　'+ ' -' *10+'\n')
print('any　'+ ' -' *10+'\n')
if any(len(item) > 2 for item in my_list)
print('ascii　'+ ' -' *10+'\n')
print('bin　'+ ' -' *10+'\n')
print('bool　'+ ' -' *10+'\n')
print('breakpoint　'+ ' -' *10+'\n')

print('bytearryay　ミュータブル（変更可）なバイト配列を返す'+ ' -' *10)
print('bytearray([1,255,50,2]):\t\t%s' % bytearray([1,255,50,2]))
print('bytearray([0x01,0xFF,0x50,0x02]):\t%s\n' % bytearray([0x01,0xFF,0x50,0x02]))
        
print('bytes　イミュータブル（変更不可）なバイト配列を返す'+ ' -' *10)
print('bytes("def", encoding="shift_jis"):\t%s\n' % bytes("def", encoding="shift_jis"))


print('callable　'+ ' -' *10+'\n')
print('chr　'+ ' -' *10+'\n')
print('classmethod　'+ ' -' *10+'\n')
print('compile　'+ ' -' *10+'\n')
print('complex　'+ ' -' *10+'\n')
print('delattr　'+ ' -' *10 +'\n')

print('dict　辞書型を返します'+ ' -' *10)
print('dict(one=1, two=2, three=3)\t%s\n' % (dict(one=1, two=2, three=3)))


# dir: 指定モジュールのメンバのリストを返す。引数が空の場合はローカルメンバのリストを返す。
# 補足：__dir__() メソッドの結果を返す
print('dir　モジュール・パッケージ内の定義内容を調べる')
print(dir(os))
print('dir(math):\t%s\n' % (dir(math)))


print('divmod　'+ ' -' *10+'\n')

print('enumerate　要素番号と要素のlist? を返す'+ ' -' *10)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print("enumerate(seasons):\t%s" % repr(list(enumerate(seasons))))
print('start =1:\t\t%s\n' % repr(list(enumerate(seasons, start=1))))

print('eval　'+ ' -' *10+'\n')
print('exec　'+ ' -' *10+'\n')
# 補足：インジェクション攻撃のリスクになりうるので eval, exec の使用は非推奨

print('filter '+ ' -' *10+'\n')
    my_filter = filter(lambda x: len(x) > 1, my_list)
    my_new_list = list(my_filter)

print('float　文字列を浮動小数点数型に変換'+ ' -' *10)
print(f'float("1.1"):\t{float("1.1")}\n')

print('format ')
print('frozenset　')
print('getattr　')
print('globals　')
print('hasattr　')
print('hash　')

# help: ヘルプの表示
print(help(os.getcwd))
print('help　')

print('hex　')
print('id　')
print('input　')

print('int　文字列を数値型に変換'+ ' -' *10)
print(f'int("65535"):\t{int("65535")}\n')

print('isinstance　')
print('issubclass　')
print('iter　')
print('len　')
print('list　')
print('locals　')
print('map ')
print('max ')
print('memoryview ')
print('min ')

print('next: iteratorの次の要素を返す。ない場合はNoneを返す')


print('object　')
print('oct　')
print('open　ファイルを開く'+ ' -' *10)
print('例文は割愛\n')

print('ord　char（Unicodeの１文字）をint にして返す'+ ' -' *10)
print("ord('c'):\t%s" % ord('c'))		# 
print("ord('C'):\t%s" % ord('C'))		# ついでに、文字列の中でクオーテーションを使いたい時は
print('ord("C"):\t%s\n' % ord("C"))		# シングルとダブルを組み合わせる事で可能となる。

print('pow　')
print('print　')
print('property　')

print('range　シークエンス型を生成する（for を用いた関数のようなものが返される）')
print("range(0,10,3):\t\t%s" % range(0,10,3))
print("list(range(0,10,3)):\t%s" % list(range(0,10,3)))
print("list(range(10)):\t%s\t※10が無い事に注目\n" % list(range(10)))

print('repr　')

print('reversed　逆順イテレータを返す')
print('list(reversed(range(3, 10, 2))):\t%s' % list(reversed(range(3, 10, 2))))
print('compare: list(range(10, 3, -2)):\t%s\n' % list(range(10, 3, -2)))

print('round')

print('set 集合型を提供する')                    # 要素を追加したり削除したりできるミュータブルな型、特に集合演算が便利
print('set([1,2,3]):\t%s\n' % set([1,2,3]))     # {1, 2, 3} となる。    s = {1, 2, 3} としてtype(s) とするとsetと返る

print('setattr　')
print('slice　')
print('sorted　')
print('staticmethod　')
print('str　')
print('sum　')
print('super　')
print('tuple　')



print('type　オブジェクトの型を返す')   # class の場合は <class 'class_name'> となる
print('type(1):\t%s\n' % type(1))     #


print('vars　')
print('zip　list要素数を最小のものに合わせる')
names = ['taro', 'hanako', 'jiro']
ages = [25, 30]
for name, age in zip(names, ages):              #
    print('name:%s    age:%s' % (name, age))    # jiro がプリントされない事に注目


