# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:29:11 2024

@author: 84372
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phưởng trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Phương trình có ngiệm là: {x}")
