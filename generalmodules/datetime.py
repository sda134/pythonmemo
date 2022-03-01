#!/usr/bin/env python
#coding: UTF-8

import datetime
from dateutil.relativedelta import relativedelta

# 基本
print(datetime)             
print("hour: %s, msec: %s" % (datetime.datetime.now().hour, datetime.datetime.now().microsecond))           
print('datetime: %s' % repr( datetime.now()))

# 文字列への変換
print("%s" % (datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))


# イニシャライザ
custom_dt = datetime.datetime(2022, 1, 23, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)


# 日時計算
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
yesterday = datetime.date.today() - datetime.timedelta(days=1)
last_month = datetime.date.today() - relativedelta(months=1)
print("tomorrow: %s, yesterday: %s" % (tomorrow, yesterday))             


# 終了
ret =input('何かキーを押してください')

