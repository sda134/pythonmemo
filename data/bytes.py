﻿#!/usr/bin/env python
#coding: UTF-8

# byte関連

byte_array1 = b'\x02\x1f\xa0'                       # 単純にバイト配列を作成する
byte_array_str1 = b"zbc"                            # 文字列からバイト配列を作成　方法1
byte_array_str2 = "test文字列".encode('utf-8')      # 文字列からバイト配列を作成　方法2
bytearray_str = bytearray("あいうえお".encode())    # bytearray(mutable:変更可能)


# 文字コードを指定しつつ16進数の文字列に変換する例
aiueo = "あいうえお".encode('utf-8', 'replace').hex()


import binascii
hexStr = str(binascii.hexlify(byte_array1), 'utf-8') # 文字列に変換する
print(hexStr)              #
print(byte_array1.hex())    # 実は同じ結果が得られる
print('"zbc:"%s' %  repr(byte_array2))

# [hex(ord(c)) for c in data]

# byte ⇔ int
iVal = 21587                                # 指定バイト数（この場合2バイト）
bytes_from_int = iVal.to_bytes(2,'big')     # を超えると例外発生
print(repr(bytes_from_int))
print('int value from bytes:%s' % int.from_bytes(bytes_from_int, 'big'))

# 二進数文字列にする関数
def bytes_to_bin(bytes):
  return [bin(b) for b in bytes]

# 関連する組み込み関数
print('bytearray([1,255,50,2]):\t\t%s' % bytearray([1,255,50,2]))
