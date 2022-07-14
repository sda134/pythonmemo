#!/usr/bin/env python
#coding: UTF-8

import datetime
from dateutil.relativedelta import relativedelta

# 基本
print(datetime)             
print("hour: %s, msec: %s" % (datetime.datetime.now().hour, datetime.datetime.now().microsecond))           
print('datetime: %s' % repr( datetime.now()))

# 今日　の取得方法
today = datetime.date.today()
today = datetime.datetime.today()


# 文字列への変換
print("%s" % (datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))

# 文字列からの変換
dt_from_str = datetime.datetime.strptime('1999-12-31 00:00:00', '%Y/%m/%d %H:%M:%S.%fff')

# イニシャライザ
custom_dt = datetime.datetime(2022, 1, 23, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)


# 日時計算
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
yesterday = datetime.date.today() - datetime.timedelta(days=1)
last_month = datetime.date.today() - relativedelta(months=1)
print("tomorrow: %s, yesterday: %s" % (tomorrow, yesterday))             


# 終了
ret =input('何かキーを押してください')

