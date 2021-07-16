#!/usr/bin/env python
#coding: UTF-8

import time
import threading


# スレッド　基本
class BasicOfThreading():
    def __init__(self):
        thread1 = threading.Thread(target=self.heavy_proccess, args=[4, 'hoge'], name='thread1')
        thread1.start()

        for k in range(5):
            time.sleep(1)
            print(thread1.is_alive())

        # 公式情報：https://docs.python.org/ja/3/library/threading.html#threading.Thread.join
        thread1.join()                          # このスレッドの終了まで待つ。

        print('the end of __init__.')



    def heavy_proccess(self, i_val, str_val):
        print(f'{threading.current_thread().name} has just started its proccess.')
        print(f'arg1 is {i_val}\targ2 is {str_val}')
        time.sleep(3)                                 # sleepの引数の単位は秒
        print('hello from heavy proccess.')


thread_basic = BasicOfThreading()
