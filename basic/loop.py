#!/usr/bin/env python
#coding: UTF-8

def frange(st, ed, step):
  while st < ed:
    yield st
    st += step


l1 = range(3) # 注意 0-2 となる
for r in l1:
    print(r)


l2 = list(frange(0.1,10.1,0.1)) # step幅を指定したlistを作成 ⇒ 0,2,4,6,8

# 二重ループ
for i in range(3):
    if i==2:
        break          # ループを抜ける
    for j in l2:
        if j==3:
            continue   # 処理をせず次のループへ
        else:
            print(i, j)

# while
i = 0
while i < 3:
    print(i)
    i += 1

# index 付きlist (dict?) enumerate　※最後の: を忘れないように
for i, v in enumerate(['tic','tac','tor']):
    print(i,v)




from enum import Enum, auto, IntEnum
class Color(IntEnum):
    RED = 1,
    GREEN = 2,
    BLUE = 3,

# enum のループ
for col in Color:
    print(col)