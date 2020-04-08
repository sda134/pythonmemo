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
