#!/usr/bin/env python
#coding: UTF-8

import poplib
import email
from email.header import decode_header

def get_header(msg, name):
    header = ''
    if msg[name]: # (ヘッダ, 文字コード) のタプルのリストで帰ってくる
        for tup in decode_header(str(msg[name])):
            if type(tup[0]) is bytes:
                charset = tup[1]
                if charset:
                    header += tup[0].decode(tup[1])
                else:
                    header += tup[0].decode()
            elif type(tup[0]) is str:
                header += tup[0]
    return header
    
    # 本文を取得
def get_content(msg):
    charset = msg.get_content_charset()
    payload = msg.get_payload(decode=True)
    try:
        if payload:
            if charset:
                return payload.decode(charset)
            else:
                return payload.decode()
        else:
            return ""
    except:
        return payload # デコードできない場合は生データにフォールバック

def fetchmail(cli, msg_no):
    content = cli.retr(msg_no)[1]
    msg = email.message_from_bytes(b'\r\n'.join(content))
    # From ヘッダ（差出人）
    from_ = get_header(msg, 'From')
    # Date ヘッダ（送信日時）
    date = get_header(msg, 'Date')
    # Subject ヘッダ（件名）
    subject = get_header(msg, 'Subject')
    # 本文
    content = get_content(msg)
    return (subject, content, from_, date)

# 参考　
# https://qiita.com/jsaito/items/a058611cf9386addbc12
# https://qiita.com/jsaito/items/5daba42f335dca7fa70b
# https://qiita.com/jsaito/items/89ea1679a9f2b99e7889

m = poplib.POP3('pop.m-tec-m.co.jp')
print('connected.')

print (m.user('isaji@m-tec-m.co.jp')) # ユーザー名入力＋結果表示
print(m.pass_('Sadahiro&929'))        # パスワード入力＋結果表示

count = len(m.list()[1])              # メール件数の把握
print('受信件数は{}件です。'.format(count))

if count > 0:

    while True:
        inpStr = input ('\nメール番号を指定して下さい[1-][q:終了]：')
        if inpStr == 'q':
            break
        else:
            try:
                reqUidl = int(inpStr)
            except ValueError as e:
                print()
            else:
                mailData = fetchmail(m, reqUidl)
                print('件名：{0[0]}\n日時：{0[3]}\n送信者：{0[2]}'.format(mailData))
                content = str(mailData[1])
                print(content)

else:
    pass

m.quit() # quit は必ずつける