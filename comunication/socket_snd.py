#!/usr/bin/env python
#coding: UTF-8

import socket

host = '192.168.1.30'
port = 6002
#snd_data = bytearray([0x30,0x30,0x30,0x30])
snd_data = "hello world".encode()
#snd_data = bytearray("あいうえお".encode())

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host,port))
soc.sendall(snd_data)
rcv_data = soc.recv(1024)
print('Received', repr(rcv_data))
soc.close()
