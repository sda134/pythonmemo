from multiprocessing import Value

# 共有メモリ上に配置する変数
shared_boolean = Value('b', True)

# 使う時
if shared_boolean.value:
    pass
