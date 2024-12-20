﻿#!/usr/bin/env python
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
# https://docs.python.org/ja/3/library/datetime.html

# 文字列からの変換
dt_from_str = datetime.datetime.strptime('1999-12-31 00:00:00.000', '%Y-%m-%d %H:%M:%S.%fff')

# date型への変換（datetime.dateにstrptimeメソッドは無い点に注意）
date_from_str = datetime.datetime.strptime('1999-12-31', '%Y-%m-%d').date()


# イニシャライザ
custom_dt = datetime.datetime(2022, 1, 23, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)


# 日時計算
# https://docs.python.org/ja/3/library/datetime.html#timedelta-objects
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
yesterday = datetime.date.today() - datetime.timedelta(days=1)
last_month = datetime.date.today() - relativedelta(months=1)
print("tomorrow: %s, yesterday: %s" % (tomorrow, yesterday))             

# タイムゾーン
utc = datetime.timezone.utc
jst = timezone(timedelta(hours=9))
jst = ZoneInfo("Asia/Tokyo")
utc_dt = datetime.datetime.now(datetime.timezone.utc)
jst_dt = utc_dt.astimezone(jst)

# 終了
ret =input('何かキーを押してください')

