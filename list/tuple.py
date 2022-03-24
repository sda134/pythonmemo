#!/usr/bin/env python
#coding: UTF-8

# リストとの違い
# immutable (変化できない)
# 実行速度がやや早い
# 
from typing import Tuple

# リスト
list_sample = [1, 2, 3, 4, 5]
 
# タプル　上下どちらでも可能
tuple_sample1 = (1, 2, 3, 4, 5)
tuple_sample1 = 1, 2, 3, 4, 5

tuple_sample1(0)                    # 値の取得

# 追加
tuple_sample2 = tuple_sample1 + (6, 7)

type_tuple = Tuple[str, str]

# 終了
ret =input('何かキーを押してください')
