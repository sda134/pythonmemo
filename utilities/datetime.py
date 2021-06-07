#!/usr/bin/env python
#coding: UTF-8

from datetime import datetime as dt

print('datetime: %s' % repr( dt.now()))



import time

for i in range(5):
    time.sleep(0.01)        # sleep関数の引数は float
    print(dt.now())
