#!/usr/bin/env python
#coding: UTF-8
    

# XML
import xml.etree.ElementTree as ET      # モジュールのインポート
tree = ET.parse('./dat/LogFields.xml')  # xmlファイルの読み込み
root = tree.getroot()

for fields in root.iter('FieldList'):
    for field in fields:
        print(field[0].text)
        print(field[1].text)





# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
#
#    # 接続
#    soc.connect((target, port))
#
#    # データ送信
#    count = soc.send(sendData)
#    
#    data = soc.recv(4)
#    print(data)
