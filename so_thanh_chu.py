# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:18:37 2024

@author: 84372
"""

so_thanh_chu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
so = int(input("Nhập một số nguyên: "))
if 0 <= so <= 9:
    print(so_thanh_chu[so])
else:
    print("Không đọc được")
   
