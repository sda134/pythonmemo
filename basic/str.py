# coding: utf-8
# 
# https://docs.python.org/ja/3/library/stdtypes.html?highlight=str#str


# 文字列操作：基本
word ='pyt' 'hon' # +なしでも連結可能（ただし初期化時のみ）
print("does't") # シングル、ダブルクォートの使い分け
print('slice1: word[0:2]%s' % word[0:2])    # スライシング（切り取り）[開始位置:終了位置]
print('slice2: word[:2] %s' % word[:2])     # 開始位置は含み、終了位置は含まない
print('slice3: word[2:] %s' % word[2:])     #
print('len：文字列長さ%s' % len(word))

# 後ろから1文字ずつ表示する例
for s in reversed(range(1, len(word) + 1)):
    letter = word[s-1:s]
    print(letter)


# 空白、文字列の削除
hoge = word.strip('p') # lstrip 左（文字列先頭）から削除
print(hoge)            # rstrip 右（文字列最後）から削除
print('- ' * 10 + '\n')


# None, 空白対応
maybe_none = None
must_be_sth = maybe_none or 'なし'          # C# の ?? みたいなにnull確認ができる


# 文字列の検索

# 注意！rfindは後ろ側の文字が優先されるだけで，index値はfindと変わらない
print('find: %s\trfind:%s' % \
    (word.find('y'), word.rfind('y')))

if 't' in word:             # True False（見つかったかどうか）のみ
    print('あるよ')

print('startwith: %s' % 'hoge'.startswith('ho'))
print('endwith: %s' % 'hoge'.endswith('ho'))

print('- ' * 10 + '\n')


# 定義済関数
import datetime
print(str(datetime.datetime.now()))  # str  直感的な文字列を返す
print(repr(datetime.datetime.now())) # repr 再利用可能な文字列を返す？19.06.13 まだよくわかってない デバッグ用出力？
print('- ' * 10)                     # 同じ文字列パターンを繰り返して表示する


# str クラスの各メソッド
list_test = "1,2,3,4,5".split(",")
count = len(list_test)     # 要素数
print(','.join(list_test)) # 結合
print('- ' * 10)


mixedStr = "abCDe"
upStr = mixedStr.upper()      # 全てを大文字へ
downStr = str.lower(mixedStr) # こんな手もある

# 文字列置き換え replace
mixedStr_re = mixedStr.replace('a', 'あ')
print('mixedStr_re %s' % mixedStr_re)


# 埋め込み   c# の string.format のようなもの
name = "guest"
score = 52.8

print('要素数は{}です'.format(count)) 
print('2番目は{0[0]}, 3番目は{0[2]}です'.format(list_test))  # 一行が長くなるので、この方法は避ける 
print("name: %s, score: %.2f" % (name, score))              # 多分これが一番メンテナンス性が良い 3.4f 整数3桁小数点4桁のfloat
print(f'using[f] - name:{name} score:{score:.3f}')          # 個々に桁数指定などをしたい場合はこれが良い？20.02.14
print('- ' * 10)



# エスケープ文字
# \n で改行　などC#と変わらないものが多い

print('a\tb\nA\tB')       # r なしで出力　結果：\t はタブ文字として認識されてしまう
print(r'a\tb\nA\tB')      # raw 文字列　C#の @ と同じ。エスケープ文字を無視する
print('￥：\\')               # エスケープ文字一覧

# ascii コード
print('ascii of [a] :%s' % ord("a"))  # アスキーコードを示す int を返す
print('ascii of [あ] :%s' % ord(u"あ"))  # 2byte 文字（uft-8) の場合


# 正規表現を使った検索
import re
re_text = "123abc456def789"
print('re.search:%s\n' %\
    re.search(r"[a-z]+", re_text))

# 終了
ret =input('何かキーを押してください')

