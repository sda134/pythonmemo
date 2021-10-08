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
print('- ' *30)


# 二重ループ
print('二重ループ') 
for i in range(3):
    if i==2:
        break               # ループを抜ける        
    for j in l2:
        if j < 2:
            print(i, j)
            continue        # 処理をせず次のループへ
else:
    print(i)                # for に付くelse：breakしなかった時に実行される

print('- ' *30)

# while
i = 0
while i < 3:
    print(i)
    i += 1

import time
print('press Ctrl+C to break')
try:
    while i < 15:
        print(i)
        i += 1
        time.sleep(1)
except KeyboardInterrupt:
    pass

print('- ' *30)




# index 付きlist (dict?) enumerate　※最後の: を忘れないように
for i, v in enumerate(['tic','tac','tor']):
    print(i,v)

print('- ' *30)



from enum import Enum, auto, IntEnum
class Color(IntEnum):
    RED = 1,
    GREEN = 2,
    BLUE = 3,

# enum のループ
for col in Color:
    print(col)

print('- ' *30)


# ループ内加工
print('all exponential:%s\n' %\
    [i**2 for i in range(-10,10)])   # 処理を施した新しいリストの作成
