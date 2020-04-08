#!/usr/bin/env python
#coding: UTF-8


# 乱数
import random

mylist = ["apple", "banana", "melon", "strawberry", "peach", "lemon"]
for i in range(5):
    print('%i 回目' % (i+1))
    print('randint:%i' % random.randint(1, 10))
    print('uniform:%f' % random.uniform(2.0,5.0))
    print('choice:%s' % random.choice(mylist))
    print('\n' + '- '*30)


random.shuffle(mylist)
print('shuffled list:%s' % mylist)

# シード値　を指定（固定乱数になる
random.seed(0)
print('randint widh seed:%i' % random.randint(1, 10))

