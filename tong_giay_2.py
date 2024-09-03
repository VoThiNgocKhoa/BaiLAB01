# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:54:56 2024

@author: 84372
"""

hh = int(input("Nhập giờ: "))
mm = int(input("Nhập phút: "))
ss = int(input("Nhập giây: "))
tong_giay = hh * 3600 + mm * 60 + ss
print(f"Tổng số giây là: {tong_giay} giây")
