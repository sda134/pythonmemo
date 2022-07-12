# coding: utf-8

import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# 小数を扱う
default_decimal = 1.234
print('type of default_decimal:%s' % type(default_decimal)))    # → float となる
explicit_decimal = Decimal(1.234)                               # 明示的にDecimal を使いたい場合の方法


# 整数で丸め


# 数値の丸めなど
print('round\t: %f' % round(1.23456789, ndigits = 2))       # 偶数への丸め
print('ceil\t: %f' % math.ceil(1.23456789))                 # 切り上げ
print('floor\t: %f' % math.floor(1.23456789))               # 切り捨て
print('//\t: %f' % (1//3))                                   # 切り捨て

#   四捨五入  ※ ROUND_HALF_UP は引数指定しなかった時のデフォルトでもある
dec_not_recommended = Decimal(1.23456789)       # floatを引数にすると、精度の悪いものを精度良く扱う為、意味が無い。
dec_val = Decimal('1.23456789')
print('quantize HALFUP\t: %f' % dec_val.quantize(Decimal("0.0001"), rounding = ROUND_HALF_UP))
print('quantize 0\t: %f' % dec_val.quantize(Decimal('0')))
print('quantize 0.1\t: %f' % dec_val.quantize(Decimal('0.1')))
print('quantize 0.01\t: %f' % dec_val.quantize(Decimal('0.01')))
print('==================')

# 2,8,16 int値を進数の文字列への変換
rawVal = 15
   yy_str = format(fiscal % 100, '02')

print('bin: %s' % bin(rawVal))
print('oct: %s' % oct(rawVal))
print('hex: %s' % hex(rawVal))
print('format: %s' % format(rawVal,'04'))       # 0n でn桁の文字列になる
print('format: %s' % (str(rawVal)).zfill(4))    # 上行と同じ結果になる
print('format b: %s' % format(rawVal,'b'))
print('format o: %s' % format(rawVal,'4o'))
print('format x: %s' % format(rawVal,'08x'))
print('.format b:{0:b}'.format(rawVal))
print('.format b:{0:4o}'.format(rawVal))
print('.format b:{0:08x}'.format(rawVal))
print('==================')


# 文字列からの変換
fval = 1.23e+16
print(fval)
print('format(arg,"f"): %f' % float('1.23456'))
print('==================')


# 2,8,16 進数の文字列を int に変換
print(int('11', 2))
print(int('11', 8))
print(int('11', 16))
print('==================')

# byte 配列⇔ 数値変換
# https://docs.python.org/ja/2.7/library/struct.html#format-characters
import struct
import ctypes

# ---- object → toBytes ----
iVal = 128
bytes16 = iVal.to_bytes(2,'big') # 128.to_bytes と直接は出来ないらしい
bytes32 = iVal.to_bytes(4,'little') # little endian  最上下位のならびかえ
print('bytes of char(1bit): %s' %  struct.pack('b', 64))
print('bytes of uchar(1bit): %s' %  struct.pack('B', 64))
print('bytes of ushort(2bit)[little]: %s' %  struct.pack('<H', 128))
print('bytes of ushort(2bit)[big]: %s' %  struct.pack('>H', 128))
print('bytes of uint(4bit): %s' %  struct.pack('I', 128))
print('bytes of long long (8bit): %s' %  struct.pack('q', 128))
print('bytes of float (4bit): %s' %  struct.pack('f', math.pi))
print('bytes of double (8bit): %s' %  struct.pack('d', math.pi))
print('bytes of various: %s' %  struct.pack('hHl', 1,2,3))
print('==================')

# ----  bytes → toNumbers ----
print('32bitMax: %s' % int.from_bytes(b'\xFF\xFF\xFF\xFF', 'big'))
print('signed16 of FFFF: %s' %struct.unpack('h', b'\xFF\xFF')[0])       # struct.unpack の戻り値は
print('unsigned16 of FFFF: %s' %struct.unpack('H', b'\xFF\xFF')[0])     #  tuple な点に注意
print('float of FFFF: %s' %struct.unpack('f', b'\xFF\xFF\xFF\xFF')[0])  # バイト数が足りないと怒られる
print('double of FFFF: %s' %struct.unpack('d', b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF')[0])
print('==================')


print (ctypes.c_uint32(4294967295).value)