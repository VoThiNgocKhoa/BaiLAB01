# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:41:42 2024

@author: 84372
"""

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
max_value = a  
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c
print(f"Giá trị lớn nhất là: {max_value}")
