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


# 数値 -> bit 配列変換
dummy_value=0x0f
bit_list= [(dummy_value & (1 << index)) > 0 for index, digit in enumerate(range(8))]

# 数値 <- bit 配列変換
val_from_bits=0
for index, bit in enumerate(bit_list):
    if bit: val_from_bits+=(0b01 << index)