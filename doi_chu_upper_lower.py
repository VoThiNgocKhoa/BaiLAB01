# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:22:12 2024

@author: 84372
"""

chu_cai = input("Nhập một chữ cái: ")
if len(chu_cai) > 1:
    print("Không hợp lệ")
else:
    if chu_cai.islower():
        print(f"Chữ cái sau khi đổi thành chữ hoa {chu_cai.upper()}")
    else:
        chu_cai.isupper()
        print(f"Chữ cái sau khi đổi thành chữ thường {chu_cai.lower()}")
