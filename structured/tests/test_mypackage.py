# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mypackage
from mypackage import *
from mypackage import class_samples, enum_samples, MyClass

mypackage.say_hello()
mypackage.say_hi()

my_cls = MyClass()
my_cls.say_myname()

# ここからは TestClass の実験
print('-' * 3 + 'TestClass' + '-' * 3)

test_cls = class_samples.TestClass()
test_cls.comment = 'comment test'
msg = test_cls.public_method('hoge')
print(msg)
test_cls._TestClass__mungled_method()     # マングリングメンバへのアクセス方法（非推奨）



# ------ 以下、検証


# イテレータの検証
#for iterItem in ts:
#    print('iter item: %s' % iterItem)
#
#print(type(ts))                         # 型の情報を表示
#print(isinstance(ts, TestClass))        # 型の確認方法
