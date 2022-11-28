import os

# https://docs.python.org/ja/3/library/functions.html

# dir: 指定モジュールのメンバのリストを返す。引数が空の場合はローカルメンバのリストを返す。
# 補足：__dir__() メソッドの結果を返す
print(dir(os))

# help: ヘルプの表示
print(help(os.getcwd))
