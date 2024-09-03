# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:37:09 2024

@author: 84372
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("Thứ tự tăng dần:", a, b, c)
N = int(input("Nhập số nguyên N: "))
N = str(N)
so_tang_dan = sorted(N)
print("Số sau khi sắp xếp các chữ số tăng dần: ", ''.join(so_tang_dan))