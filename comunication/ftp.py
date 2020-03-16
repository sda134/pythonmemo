#!/usr/bin/env python
#coding: UTF-8

import ftplib
 
 # https://docs.python.org/ja/3/library/ftplib.html 公式書類

## FTP情報 
HOST = '192.168.1.11'
PORT = 5011
USER = 'admin' 
PASSWORD = 'admin' 
DIRECTORY = r'Package1\LOG00001' 

ftp = ftplib.FTP()
ftp.connect(HOST)          # ポートの指定なしで接続
#ftp.connect(HOST, PORT)   # ホスト、ポートを指定して接続 
ftp.login(USER, PASSWORD)  # ユーザID、パスワードを指定してログイン 
ftp.dir()                  # ファイルやフォルダのリストをコンソールに表示
items = ftp.mlsd()

ftp.cwd(DIRECTORY)         # 指定のディレクトリに移動 
ftemp = ftp.nlst('.')      # 指定ディレクトリ内のファイル名のリストを取得
    
for file in ftemp:
    print(file)
    length = len(file)
    fn_g2l = file[0:(length-3)]
    fn_g2l = fn_g2l + 'G2L'     # ftp.delete で消そうとしたが出来なかった 19.06.12

    with open(file, 'wb') as f:    # open の第一引数は、保存ファイル名
        ftp.retrbinary ('RETR %s' % file, f.write)
        #ftp.delete(file) # ファイルを削除する

ftp.quit()
input('何かボタンを押してください')
