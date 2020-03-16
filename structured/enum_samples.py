#!/usr/bin/env python
#coding: UTF-8

from enum import Enum, auto, IntEnum

# auto について
# 以下の様に使用する。※あんま意味ない気がするが
"""
class Color(IntEnum):
    RED   = auto(),    
    GREEN = auto(),    ...
"""

# 基本のEnum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

clr = Color.RED
print('完全なenum 名 が欲しい時: %s' % clr)
print('enum 名だけ が欲しい時: %s' % clr.name)
print('int 値 が欲しい時: %i' % clr.value)


# EnumはあくまでEnum型として扱われるが、IntEnum はint
# 同名の Enumメンバは不可だが、同じint 値を持つメンバは作成可
class Animal(IntEnum):
    DOG = 1,
    CAT = 2,
    BIRD = 3,

    def describe(self):         # C# の拡張メソッドのような事ができる
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_animal(cls):
        return cls.DOG


# ====== 実際の利用 ======
# enum のループ
for col in Color:
    print('in loop  val:%s' % col)
for name, member in Color.__members__.items():
    print('name:%s\tmember:%s ' % (name, repr(member)))
print('---------')

# enum のハッシュ利用
apples = {}
apples[Color.RED] = 'delicious'
apples[Color.GREEN] = 'granny smith'
print('red apples are %s' % apples[Color.RED])
print('-' * 30)

# 様々なアクセス方法
print(Color(1))
print(Color['RED'])
print(list(Color))    # list化も可能
print('-' * 30)



print(Animal.favorite_animal())
print(Animal.DOG.describe())
print('-' * 30)


# 条件判断
if clr is Color.RED:
    print('clr is RED')
else:
    pass