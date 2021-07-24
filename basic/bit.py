#!/usr/bin/env python
#coding: UTF-8


# 論理積
bit_and = 0b1111 & 0b0101
print('論理積:' + bin(bit_and))

# 論理和
bit_or = 0b0100 | 0b1010
print('論理積:' + bin(bit_or))

# ビットシフト
left_shifted = 0b0101 << 1
print('左シフト:' + bin(left_shifted))

left_shifted <<= 3  
print('再度左シフト:' + bin(left_shifted))

right_shifted = 0b1010 >> 1
print('右シフト:' + bin(right_shifted))

