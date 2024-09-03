# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:11:47 2024

@author: 84372
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
min_value = a
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d
print(f"Giá trị nhỏ nhất là: {min_value}")
        

