# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:08:26 2024

@author: NgocKhoa 
"""

import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tu = ((a + b)/(math.pow(a, 1/3) + math.pow(b, 1/3))) - (math.pow(a*b, 1/3))
mau = (math.pow(a, 1/3) - math.pow(b, 1/3)) ** 2
bieu_thuc = tu/mau
print(f"Giá trị biểu thức là: {bieu_thuc}")