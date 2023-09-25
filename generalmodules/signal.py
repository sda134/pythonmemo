#!/usr/bin/env python3
#coding: UTF-8

import signal
import time


def scheduler(arg1, args2):
    print(time.time())

signal.signal(signal.SIGALRM, scheduler)    # 補足：Linux環境でないと使えない
signal.setitimer(signal.ITIMER_REAL, 1, 1)
time.sleep(1000)