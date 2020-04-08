#!/usr/bin/env python
#coding: UTF-8

import subprocess

def ping(hosts):
    result = []
    for host in hosts:
        # pingコマンド
        pg = subprocess.Popen(["ping", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # ping試験
        out, error = pg.communicate()
        print("■" + host)
        print("----------------------")
        print(out.decode('Shift-JIS'))
        print("----------------------")
        result.append(out.decode('Shift-JIS'))


ping(['10.4.1.110', '10.4.1.111'])